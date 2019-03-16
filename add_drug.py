from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class AddDrugForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    discript = TextAreaField('Описание', validators=[DataRequired()])
    number = IntegerField('Количество', validators=[DataRequired()])
    submit = SubmitField('Добавить')