import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


import requests

# Where USD is the base currency you want to use
url = 'http://api.exchangeratesapi.io/v1/latest?access_key=1896b2be48dacf88b405e92f6d2136fe&symbols=USD,TRY'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)

USD=data["rates"]["USD"]
TRY=data["rates"]["TRY"]
print(USD)
print(TRY)

@app.route("/")
def home():
    """ the main view of the app """
    return render_template("main.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
