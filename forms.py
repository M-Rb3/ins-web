from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField, TextAreaField, RadioField, SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError


class PredictForm(FlaskForm):
    age = IntegerField('Age')
    sex = RadioField('Gender', choices=[
        'male', 'female'])
    bmi = DecimalField('BMI')
    children = IntegerField('Children')
    smoker = RadioField('smoking Status', choices=[
        'yes', 'no'])
    region = SelectField(choices=[
        'northeast', 'southeast', 'northwest', 'southwest'])
    submit = SubmitField('Predict')
    abc = ""  # this variable is used to send information back to the front page
