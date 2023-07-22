from flask import Flask, render_template
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

django_api_base_url = "http://127.0.0.1:8000/api/"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/personas")
def personas():
    r = requests.get(django_api_base_url + "personas/", auth=(usuario, clave))
    data = json.loads(r.content)['results']
    return render_template("data.html", data=data, title='Personas')

@app.route("/barrios")
def barrios():
    r = requests.get(django_api_base_url + "barrios/", auth=(usuario, clave))
    data = json.loads(r.content)['results']
    return render_template("data.html", data=data, title='Barrios')

@app.route("/locales_comida")
def locales_comida():
    r = requests.get(django_api_base_url + "locales_comida/", auth=(usuario, clave))
    data = json.loads(r.content)['results']
    return render_template("data.html", data=data, title='Locales Comida')

@app.route("/locales_repuestos")
def locales_repuestos():
    r = requests.get(django_api_base_url + "locales_repuestos/", auth=(usuario, clave))
    data = json.loads(r.content)['results']
    return render_template("data.html", data=data, title='Locales Repuestos')

if __name__ == "__main__":
    app.run(debug=True)
