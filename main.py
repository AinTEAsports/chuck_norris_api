import json
import random
import requests

from flask import Flask


app = Flask(__name__)

LANGUAGES_INFORMATIONS = {
    "fr" : {
        "upper" : "FR",
        "lower" : "fr",
        "english_name" : "french",
        "native_name" : "français",
        "path" : "/fr",
        "help_path" : "/fr/help",
    },
    
    "en" : {
        "upper" : "EN",
        "lower" : "en",
        "english_name" : "english",
        "native_name" : "english",
        "path" : "/en",
        "help_path" : "/en/help",
    }
}

AVAILIBLE_LANGUAGES = [language for language in LANGUAGES_INFORMATIONS]

CREDITS_INFORMATIONS = {
    "aintea" : {
        "discord" : "AinTea#0519",
        "github" : "https://github.com/AinTEAsports",
        "instagram" : None,
        "twitter" : None,
        "snapchat" : None,
        "facebook" : None,
        "spotify" : None,
        "linkedin" : None,
    }
}


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


@app.route("/languages", methods=["GET"])
def get_languages():
    languages = {"languages" : AVAILIBLE_LANGUAGES}
    return json.dumps(languages)


@app.route("/languages_informations", methods=["GET"])
def get_languages_informations():
    return json.dumps(LANGUAGES_INFORMATIONS)


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
