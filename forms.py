from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('nombre_usuario', validators=[DataRequired()], render_kw={"placeholder": "Nombre de Usuario",'class': 'form-control'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder": "Contraseña", 'class': 'form-control'})
    submit = SubmitField('Iniciar Sesion', render_kw={ 'class': 'btn btn-primary col-sm-12 col-md-6'})

class RegistroForm(FlaskForm):
    nombre  = StringField('Nombres ', validators=[DataRequired('Ingrese Nombres')])
    apellido  = StringField('Apellidos', validators=[DataRequired('Ingrese su Apellido')])
    correo  = StringField('Correo Electrónico', validators=[DataRequired('Ingrese su correo electrónico'),Email('Ingrese un Correo Válido') ])
    nombreusuario  = StringField('Nombre de Usuario', validators=[DataRequired('Ingrese un Nombre de Usuario')])
    password = PasswordField('Contraseña', validators=[DataRequired('Ingrese su contraseña')])
    tienda  = StringField('Nombre de la Tienda', validators=[DataRequired('Ingrese el Nombre de la Tienda')])
    nit  = StringField('NIT', validators=[DataRequired('Ingrese el NIT de la Tienda')])
    direccion  = StringField('Direccion', validators=[DataRequired('Ingrese la dirección de la Tienda')])
    telefono  = StringField('Teléfono', validators=[DataRequired('Ingrese el Teléfono de la Tienda')])
    ciudad  = StringField('Ciudad', validators=[DataRequired('Ingrese la Ciudad')])
    submit = SubmitField('Registrar Tienda', render_kw={ 'class': 'btn btn-primary col-sm-12 col-md-6'})