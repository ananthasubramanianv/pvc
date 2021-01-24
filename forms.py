from flask_wtf import Form
from wtforms import TextField, SubmitField, RadioField, DateField, FloatField
from wtforms import validators

class PoldetailsForm(Form):
    polnum = TextField("Policy Number", [validators.DataRequired()])
    premium = FloatField("Premium",  [validators.DataRequired()])
    poldat = DateField("Policy Start Date",  [validators.DataRequired()])
    membership = RadioField('Membership', choices=[('Y', 'Yes'), ('N', 'No')])
    submit = SubmitField("Submit")


