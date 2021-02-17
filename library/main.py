from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form.get("book_name")
        book_author = request.form.get("book_author")
        book_rating = request.form.get("book_rating")

        new_book = Book(title=book_name, author=book_author, rating=book_rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(location=url_for("home"))
    return render_template("add.html")


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form["id"]
        new_rating = request.form["new_rating"]
        book_selected = Book.query.get(book_id)
        book_selected.rating = new_rating
        db.session.commit()
        return redirect(location=url_for("home"))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route('/delete', methods=['GET'])
def delete():
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(location=url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

