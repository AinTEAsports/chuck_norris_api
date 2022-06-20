import os
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
    },
    
    "en" : {
        "upper" : "EN",
        "lower" : "en",
        "english_name" : "english",
        "native_name" : "english",
        "path" : "/en",
    }
}

AVAILIBLE_LANGUAGES = [language.upper() for language in LANGUAGES_INFORMATIONS]

CREDITS_INFORMATIONS = {
    "aintea" : {
        "role" : "developer",
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
            {' - '.join(AVAILIBLE_LANGUAGES)}
        </b>
    </center>"""


@app.route("/credits/<person>")
def get_credits(person : str = ""):
    person = person.lower()
    
    if not person in CREDITS_INFORMATIONS.keys():
        return ""
    
    if not person:
        return json.dumps(CREDITS_INFORMATIONS)
    
    return json.dumps(CREDITS_INFORMATIONS[person])


@app.route("/languages", methods=["GET"])
def get_languages():
    languages = {"languages" : AVAILIBLE_LANGUAGES}
    return json.dumps(languages)


@app.route("/languages_informations/<language>", methods=["GET"])
def get_languages_informations(language : str = ""):
    if language not in LANGUAGES_INFORMATIONS.keys():
        return ""
    
    if not language:
        return json.dumps(LANGUAGES_INFORMATIONS)
    
    return json.dumps(LANGUAGES_INFORMATIONS[language])


@app.route("/help", methods=["GET"])
def get_help() -> str :
    return ""


@app.route("/joke/<language>", methods=["GET"])
def get_joke(language : str = "en") -> str :
    language = language.lower()
    
    if language == "en":
        response = requests.get("https://api.chucknorris.io/jokes/random")
        joke = json.loads(response.text)["value"]
        
        return joke
    
    if not f"{language}.txt" in os.listdir("jokes/"):
        return ""
    
    with open(f"jokes/{language}.txt", 'r') as f:
        jokes = f.readlines()

    if not jokes:
        return ""
    
    return random.choice(jokes)


app.run(debug=True)
