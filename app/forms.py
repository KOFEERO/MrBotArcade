from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Optional
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField


################ (FORMULARIO MAQUINAS) ################
class RegisterMachine(FlaskForm):
    name = StringField('Nombre de la maquina')
    ip = StringField('IP de la maquina')
    description = TextAreaField('Descripcion')
    submit = SubmitField()

class TimeForm(FlaskForm):
    description = TextAreaField('Descripcion', validators=[Optional()])
    hour = StringField('Hour', validators=[DataRequired(), Length(min=1, max=1)])
    minute = StringField('Minute', validators=[DataRequired(), Length(min=1, max=1)])
    price_time = IntegerField('Price time', validators=[DataRequired()])
    submit = SubmitField()


class ResetTime(FlaskForm):
    machines = SelectField('Maquinas', validators=[DataRequired()])
    reset_time = SubmitField('Reseatear tiempo')
