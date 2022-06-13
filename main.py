import json
import random
import requests

from flask import Flask


app = Flask(__name__)


@app.route("/")
def root():
    return ""


@app.route("/en", methods=["GET"])
def en() -> str :
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = json.loads(response.text)["value"]
    
    return joke


@app.route("/fr", methods=["GET"])
def fr() -> str :
    with open("./chuck_jokes_fr.txt", 'r') as f:
        jokes = f.readlines()
    
    if not jokes:
        return ""
    
    return random.choice(jokes)


app.run(debug=True)
