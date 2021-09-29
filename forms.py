from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('nombre_usuario', validators=[DataRequired()], render_kw={"placeholder": "Nombre de Usuario",'class': 'form-control'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder": "Contraseña", 'class': 'form-control'})
    submit = SubmitField('Iniciar Sesion', render_kw={ 'class': 'btn btn-primary col-sm-12 col-md-6'})
