from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, HiddenField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("API_KEY")
search_endpoint = os.getenv("API_SEARCH_ENDPOINT")
detail_endpoint = os.getenv("API_DETAILS_ENDPOINT")
image_endpoint = os.getenv("IMAGE_ENDPOINT")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.Text, nullable=True)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, "
#                 "pinned down by an extortionist's sniper rifle. "
#                 "Unable to leave or receive outside help, Stuart's negotiation with the caller "
#                 "leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()


class RateMoviesForm(FlaskForm):
    rating = FloatField(label="Your Rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    id = HiddenField()
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMoviesForm()
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        selected_movie.rating = float(form.rating.data)
        selected_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=selected_movie, form=form)


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    db.session.delete(selected_movie)
    db.session.commit()

    return redirect(location=url_for("home"))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovieForm()

    if form.validate_on_submit():
        movie_name = form.movie_title.data
        params = {
            "api_key": key,
            "query": movie_name
        }
        response = requests.get(url=search_endpoint, params=params)
        movies = response.json()["results"]
        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)


@app.route("/select", methods=['GET', 'POST'])
def select():
    params = {
        "api_key": key,
    }
    movie_id = request.args.get('id')
    response = requests.get(url=detail_endpoint+movie_id, params=params)
    movie_details = response.json()
    print(movie_details)
    year = movie_details['release_date'].split('-')[0]
    new_movie = Movie(
        title=movie_details['title'],
        year=year,
        description=movie_details['overview'],
        rating=None,
        ranking=None,
        review=None,
        img_url=image_endpoint+movie_details['poster_path'],
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(location=url_for("edit"), movie=selected_movie)


if __name__ == '__main__':
    app.run(debug=True)
