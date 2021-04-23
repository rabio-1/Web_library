from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class CommentsCreateForm(FlaskForm):
    text = StringField('Введите коментарий', validators=[DataRequired()])
    submit = SubmitField('Отправить')