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
    rndm = random.randint(-100, 100)
    random_list.append(rndm)
    for count, ele in enumerate(random_list):
        if count != 0:
            if ele < (count - 1):
                decreas_count += 1
                increas_count = 0
            elif ele > (count - 1):
                increas_count += 1
                decreas_count = 0
    print(decreas_count)
    print(increas_count)
    return random_list


@app.route("/")
def home():
    """ the main view of the app """
    threading.Timer(10, random_number())


    # total_sum = sum(random_list)
    return render_template("main.html", random_list=random_list,
                           )


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
