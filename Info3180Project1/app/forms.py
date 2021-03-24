from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DecimalField, FileField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect
from flask import Flask

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    csrf.init_app(app)

housetypes = ["House","Apartment"]
class CreatePropertyForm(FlaskForm):

    propertyname = StringField('Property Title', validators=[DataRequired()])

    descrip = TextAreaField('Description', validators=[DataRequired()])

    numroom = StringField('No. of Rooms', validators=[DataRequired()])

    numbathroom = StringField('No. of Bathrooms', validators=[DataRequired()])

    price = DecimalField('Price', validators=[NumberRange(min=0, max=None,message=None)])

    proptype = SelectField('Property Type', choices=housetypes, validators=[DataRequired()])

    address = StringField('Location', validators=[DataRequired()])

    photo = FileField('Photo')

    hiddenid = HiddenField('hiding')

    submitbtn = SubmitField("Add Property")