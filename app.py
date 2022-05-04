import os
from flask import Flask, render_template
import requests
import random
import time
import threading
if os.path.exists("env.py"):
    import env


app = Flask(__name__)



# Where USD is the base currency you want to use
url = 'http://api.exchangeratesapi.io/v1/latest?access_key=1896b2be48dacf88b405e92f6d2136fe&symbols=USD,TRY'

# Making our request
# response = requests.get(url)
# data = response.json()

# Your JSON object
# print(data)

# USD=data["rates"]["USD"]
# TRY=data["rates"]["TRY"]
# print(USD)
# print(TRY)
random_list = [10]
initial_capital = 100


def random_number():
    """ dummy function to generate random numbers """
    decreas_count = 0
    increas_count = 0
    shift_up = 0
    shift_down = 0
    rndm = random.randint(-100, 100)
    random_list.append(rndm)
    for count, ele in enumerate(random_list):
        if count != 0:
            if ele < (count - 1):
                decreas_count += 1
                if increas_count > 3:
                    shift_down = 1
                shift_up = 0
                increas_count = 0
            elif ele > (count - 1):
                increas_count += 1
                if decreas_count > 3:
                    shift_up = 1
                shift_down = 0
                decreas_count = 0

    if decreas_count > 3:
        print("down trend")
    if increas_count > 3:
        print("up trend")
    print("Decrease " + str(decreas_count))
    print("Increase " + str(increas_count))
    print("shift up = " + str(shift_up))
    print("shift down = " + str(shift_down))
    if shift_up > 0:
        shift_up = 0
        print("shift up")
    if shift_down > 0:
        shift_down = 0
        print("shift down")

    return random_list


@app.route("/")
def home():
    """ the main view of the app """
    threading.Timer(3, random_number())
    capital = initial_capital

    # total_sum = sum(random_list)
    return render_template("main.html", random_list=random_list,
                           capital=capital)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
