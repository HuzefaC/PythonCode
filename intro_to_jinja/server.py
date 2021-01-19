from flask import Flask, render_template
from _datetime import datetime
import requests

app = Flask(__name__)
current_year = datetime.now().year


@app.route("/")
def home_page():
    return render_template("index.html", current_year=current_year)


@app.route("/guess/<name>")
def name_gender(name):
    response_age = requests.get(f"https://api.agify.io?name={name}").json()
    age = response_age["age"]
    response_gender = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = response_gender["gender"]
    return render_template("name_gender.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
