from flask import Flask
app = Flask(__name__)



@app.route('/bye')
def bye():
    return 'Bye'


@app.route('/')
def hello_world():
    return 'Hello, World!'
def make_bold(function):
    pass


@app.route('/<name>/<int:num>')
def hello(name, num):
    return f"Hello {name}. Number is {num}"


if __name__ == "__main__":
    app.run(debug=True)
