from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    coffee_rating_choices = ["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
    wifi_rating_choices = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    power_rating_choices = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 8PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=coffee_rating_choices,
                                validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Strength Rating', choices=wifi_rating_choices,
                              validators=[DataRequired()])
    power_outlet_rating = SelectField(label='Power Outlet Availability',
                                      choices=power_rating_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    data = [form.cafe.data, form.location.data, form.open_time.data, form.closing_time.data,
            form.coffee_rating.data, form.wifi_rating.data, form.power_outlet_rating.data]
    if form.validate_on_submit():
        with open('cafe-data.csv', newline='', encoding="utf-8", mode="a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
