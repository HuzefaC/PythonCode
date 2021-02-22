from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as r

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# HTTP GET - Read Record
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET'])
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = r.choice(cafes)
    # cafe = {
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "has_sockets": random_cafe.has_sockets,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "seats": random_cafe.seats,
    #     "coffee_price": random_cafe.coffee_price
    # }
    return jsonify(random_cafe.to_dict())


@app.route("/all", methods=['GET'])
def all_cafes():
    cafes_db = db.session.query(Cafe).all()
    cafes = []
    for cafe in cafes_db:
        cafes.append(cafe.to_dict())

    all_cafe_dict = {
        "cafes": cafes
    }
    return jsonify(all_cafe_dict)


@app.route("/search", methods=['GET'])
def search():
    errors = [
        {
            "error_not_found": {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        },
        {
            "error_invalid_url": {
                "Not Found": "Sorry, invalid URL"
            }
        }
    ]

    location = request.args.get('loc')

    if location is None:
        return jsonify(errors[1])

    cafes_db = db.session.query(Cafe).all()
    cafes = []
    for cafe in cafes_db:
        if cafe.location.lower() == location.lower():
            cafes.append(cafe.to_dict())
    if cafes:
        return jsonify(cafes)
    else:
        return jsonify(errors[0])


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.args.get('name'),
        map_url=request.args.get('map_url'),
        img_url=request.args.get('img_url'),
        location=request.args.get('location'),
        seats=request.args.get('seats'),
        has_toilet=bool(request.args.get('has_toilet')),
        has_wifi=bool(request.args.get('has_wifi')),
        has_sockets=bool(request.args.get('has_sockets')),
        can_take_calls=bool(request.args.get('can_take_calls')),
        coffee_price=request.args.get('coffee_price'))

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    selected_cafe = Cafe.query.get(cafe_id)
    if selected_cafe:
        new_price = request.args.get('new_price')
        selected_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": f"Successfully updated the cafe {selected_cafe}."})
    else:
        return jsonify(response={"error": {"Not Found": "Sorry a cafe with that "
                                                        "id was not found in our database."}
                                 })


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete(cafe_id):
    selected_cafe = Cafe.query.get(cafe_id)
    if selected_cafe:
        api_key = str(request.args.get('api-key'))
        if api_key == "123456789":
            db.session.delete(selected_cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully updated the cafe {selected_cafe}."})
        else:
            return jsonify(response={"error": {"Access Denied": "Sorry you are not authorized "
                                                                "to delete a cafe from our database."}
                                     })
    else:
        return jsonify(response={"error": {"Not Found": "Sorry a cafe with that "
                                                        "id was not found in our database."}
                                 })


if __name__ == '__main__':
    app.run(debug=True)
