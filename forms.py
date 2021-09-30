from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('nombre_usuario', validators=[DataRequired()], render_kw={"placeholder": "Nombre de Usuario",'class': 'form-control'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder": "Contraseña", 'class': 'form-control'})
    submit = SubmitField('Iniciar Sesion', render_kw={ 'class': 'btn btn-primary col-sm-12 col-md-6'})

class RegistroForm(FlaskForm):
    nombre  = StringField('nombre', validators=[DataRequired()], render_kw={"placeholder": "Nombres Completos",'class': 'form-control'})
    apellido  = StringField('apellido', validators=[DataRequired()], render_kw={"placeholder": "Apellido de Usuario",'class': 'form-control'})
    correo  = StringField('correo', validators=[DataRequired()],  render_kw={"placeholder": "Correo Electrónico",'class': 'form-control'})
    nombreusuario  = StringField('nombreusuario', validators=[DataRequired()], render_kw={"placeholder": "Nombre Usuario",'class': 'form-control'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder": "Contraseña",'class': 'form-control'})
    tienda  = StringField('tienda', validators=[DataRequired()], render_kw={"placeholder": "Nombre de la Tienda",'class': 'form-control'})
    nit  = StringField('nit', validators=[DataRequired()], render_kw={"placeholder": "NIT",'class': 'form-control'})
    direccion  = StringField('direccion', validators=[DataRequired()], render_kw={"placeholder": "Dirección",'class': 'form-control'})
    telefono  = StringField('telefono', validators=[DataRequired()], render_kw={"placeholder": "Teléfono",'class': 'form-control'})
    ciudad  = StringField('ciudad', validators=[DataRequired()], render_kw={"placeholder": "Ciudad",'class': 'form-control'})
    submit = SubmitField('Registrar Tienda', render_kw={ 'class': 'btn btn-primary col-sm-12 col-md-6'})