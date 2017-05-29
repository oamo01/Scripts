from wtforms import Form, StringField, IntegerField, FloatField
from wtforms import validators


class CommentForm(Form):
	username = FloatField('Flujo', [validators.NumberRange(min=0, max=5.02, message='Introduce un dato adecuado.')
									, validators.Required(message='Introducir un flujo')])
