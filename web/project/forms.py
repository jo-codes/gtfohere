from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid
import flask

class Reg(FlaskForm):

	name = wtf.StringField("Name")
	date = wtf.DateField("Date", validators=[valid.DataRequired("Dates can't be empty")])
	money = wtf.IntegerField("Sum", validators=[valid.DataRequired("Sum can't be empty")])

	submit = wtf.SubmitField("Get options")

