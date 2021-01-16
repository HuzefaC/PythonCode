from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0, 9)


@app.route('/')
def home_route():
    return "<h1 style='color: green;'>Enter a number between 0-9 in URL</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route('/<int:num>')
def random_number(num):
    num = int(num)
    if num == random_num:
        return "<h1 style='color: green;'>You found me</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"
    elif num > random_num:
        return "<h1 style='color: red;'>Too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    else:
        return "<h1 style='color: red;'>Too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)
