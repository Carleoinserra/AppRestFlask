from flask import Flask, render_template, request, make_response
import mysql.connector
from matplotlib import pyplot as plt
from stripe._http_client import requests
from translate import Translator
import io
def truncate_text(text, max_length=500):
    if len(text) > max_length:
        return text[:max_length] + '...'
    return text
app = Flask(__name__)

@app.route("/")
def store():



    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)

    if response.status_code == 200:
        # Crea un'istanza del traduttore

        data = response.json()
        print(data)

        # Crea un'istanza del traduttore





        #return("hello")
        return render_template('prod.html' , prod = data)
    else:
        return f"Errore {response.status_code}"
import random

@app.route("/mario")
def mario():
    marioRandom = (random.randint(1, 15))

    url = "https://www.amiiboapi.com/api/amiibo/?name=%20mario"
    response = requests.get(url)

    if response.status_code == 200:
        # Crea un'istanza del traduttore

        data = response.json()
        marioP = (data['amiibo'][marioRandom])

        # Crea un'istanza del traduttore





        #return("hello")
        return render_template('prodM.html' , prod = marioP)
    else:
        return f"Errore {response.status_code}"



if __name__ == '__main__':

   app.run(debug = True)