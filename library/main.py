from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        book_name = request.form.get("book_name")
        book_author = request.form.get("book_author")
        book_rating = request.form.get("book_rating")
        new_book = {
            "title": book_name,
            "author": book_author,
            "rating": book_rating
        }
        all_books.append(new_book)
        return redirect(location=url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

