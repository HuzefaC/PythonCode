from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
response = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
posts = response.json()


@app.route('/')
def index():
    return render_template("index.html", posts=posts)


@app.route('/index.html')
def home():
    return render_template("index.html", posts=posts)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_mail(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_mail(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\n" \
                              f"Phone: {phone}\nMessage:{message}"

    my_email = os.getenv("email")
    my_password = os.getenv("password")
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(my_email, my_password)
        connection.sendmail(my_email, my_email, email_message)


if __name__ == "__main__":
    app.run(debug=True)
