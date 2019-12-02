from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  CA = StringField('Coded aperture name', validators=[DataRequired()])
  author = StringField('Author name', validators=[DataRequired()])
  assoc = StringField('Association', validators=[DataRequired()])
  #mask = SubmitField('Upload mask')
  submit = SubmitField('Submit')