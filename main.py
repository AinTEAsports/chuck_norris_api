import json
import random
import requests

from flask import Flask


app = Flask(__name__)

AVAILIBLE_LANGUAGES = [
    "FR",
    "EN",
]


@app.route("/")
def root():
    return f"""<center>
        Here are the languages present on this API:
        
        <br>
        <br>
        
        <b>
            {' '.join(AVAILIBLE_LANGUAGES)}
        </b>
    </center>"""


@app.route("/en", methods=["GET"])
def en() -> str :
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = json.loads(response.text)["value"]
    
    return joke


@app.route("/en/help", methods=["GET"])
def en_help() -> str :
    return ""


@app.route("/fr", methods=["GET"])
def fr() -> str :
    with open("./chuck_jokes_fr.txt", 'r') as f:
        jokes = f.readlines()
    
    if not jokes:
        return ""
    
    return random.choice(jokes)


@app.route("/fr/help", methods=["GET"])
def fr_help() -> str :
    return ""


app.run(debug=True)
