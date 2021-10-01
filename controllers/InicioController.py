from flask import Flask, session
from app import Bcrypt ,bcrypt, mail

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.categoria import Categoria
from models.producto import Producto
from models.usuario import Usuario
from models.tienda import Tienda

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import LoginForm, RegistroForm

from flask_mail import  Message
from flask_session import Session

# app = Flask(__name__)
# app.config.from_object('config')

# @login_required
def home():
    # print("Actual logueado", current_user)
    user = Usuario.query.filter_by(id=current_user.id).first()
    # print(user)
    categoriasTotal = Categoria.count_records(user.id_tienda)
    productosTotal = Producto.count_records(user.id_tienda)  

    tienda = Tienda.query.filter_by(id=user.id_tienda).first()
    nombredetienda = tienda.nombre_tienda
    nitdetienda = tienda.nit
    direcciondetienda = tienda.direccion
    telefonodetienda = tienda.telefono

    usuariosInactivos = 0
    if Usuario.count_records_inacticos() > 0:
        usuariosInactivos = Usuario.count_records_inacticos()
    session['inactivos'] = usuariosInactivos
    print("Inactivos",usuariosInactivos)

    return render_template('/home.html', totalcategoria=categoriasTotal, totalproducto=productosTotal, nombretienda = nombredetienda, nittienda = nitdetienda, direcciontienda = direcciondetienda, telefonotienda = telefonodetienda, inactivos=usuariosInactivos) 

def index():
    
    return render_template('/index.html')

def frmRegistrarTienda():
    registroTienda = RegistroForm()
    print(registroTienda)
    if registroTienda.validate_on_submit():
        print(registroTienda.nombre.data)
        _nombre = registroTienda.nombre.data
        _apellido = registroTienda.apellido.data
        _correo = registroTienda.correo.data
        _nombreusuario = registroTienda.nombreusuario.data
        _password = bcrypt.generate_password_hash(registroTienda.password.data).decode('utf-8')
        _tienda = registroTienda.tienda.data
        _nit = registroTienda.nit.data
        _direccion = registroTienda.direccion.data
        _telefono = registroTienda.telefono.data
        _ciudad = registroTienda.ciudad.data
        _propietario = str(_nombre) + str(_apellido)
        _id_usuario = request.form.get('txtId')

        nuevaTienda = Tienda(_tienda, _nit, _direccion, _telefono, _propietario, _ciudad)
        print(nuevaTienda)
        idtienda = nuevaTienda.save()

        usuario = Usuario(_id_usuario,_nombre, _apellido, _correo, _nombreusuario, _password, "Tendero")
        usuario.activo = 1
        usuario.id_tienda = idtienda
        print(usuario)
        usuario.save()

        mailtotendero(_nombre, _apellido, _correo, _tienda)
        # if idtienda > 1:
        return render_template("index.html")

    # flash('Enviando Datos', 'success')
    # else:
    #     print("No ingresa a validar")
    #     print(registroTienda.nombre.data)
    return render_template("registrotienda.html", form=registroTienda)

def frmlogin():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        _nombre = login_form.username.data
        _password = login_form.password.data



        passIngresado=bcrypt.generate_password_hash('_password').decode('utf-8')
        print("Ingresado", _nombre, _password,passIngresado)
        print("Ingresado", passIngresado)
        user = Usuario.query.filter_by(nombre_usuario=_nombre).first()
        print("Usuario Activo = ", user.is_active)
        if (user.is_active==False):
            flash('Usuario Inactivo', 'success')
            return render_template("index.html")

        print(user)
        if not user:
            session.pop('_flashes', None)
            flash(f'Usuario no encontrado en la Base de Datos!', 'danger')
            
        else:
            passUsuario = user.password
            print("Encontrado")

        
            print("Usuario",user.nombre, user.apellidos,  passUsuario)
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            flash('Bienvenido de Regreso', 'success')


            n = login(_nombre)

            next = request.args.get('next', None)
            if next:
                return redirect(next)     
            return n       
        else:
            session.pop('_flashes', None)
            flash(f'Inicio de Sesion incorrecto, verifique el Usuario y Contraseña!', 'danger')

    return render_template("login.html", form=login_form)



    # return render_template('/login.html', form = login_form )    


# @login_required
def logout():
    logout_user()
    return render_template('index.html') 
    #return 'You are now logged out!'    


def login(nombre):
 
    print(bcrypt.generate_password_hash('_password'))
    #print(_nombre)
    user = Usuario.query.filter_by(nombre_usuario=nombre).first()
    #print(user)

    login_user(user)
    id_tienda_usuario = user.id_tienda
    categoriasTotal = Categoria.count_records(id_tienda_usuario)
    productosTotal = Producto.count_records(id_tienda_usuario)  
    tienda = Tienda.query.filter_by(id=id_tienda_usuario).first()
    nombredetienda = tienda.nombre_tienda
    nitdetienda = tienda.nit
    direcciondetienda = tienda.direccion
    telefonodetienda = tienda.telefono

    
    usuariosInactivos = 0
    if Usuario.count_records_inacticos() > 0:
        usuariosInactivos = Usuario.count_records_inacticos()
    
    session['inactivos'] = usuariosInactivos

    print("Usuarios Inactivos", usuariosInactivos)
    if(user.rol=="Administrador"):
        return redirect('/usuario')    
    return render_template('home.html', totalcategoria=categoriasTotal, totalproducto=productosTotal, nombretienda = nombredetienda, nittienda = nitdetienda, direcciontienda = direcciondetienda, telefonotienda = telefonodetienda)
    #return 'You are now logged in!'       

def mailtoadmin():
    msg = Message('Hello from the other side!', sender = 'peter@mailtrap.io', recipients = ['sergioess@hotmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    mail.send(msg)
    return "Message sent!"


def mailtotendero(nombre, apellido, correo, tienda):
    msg = Message('Tienda Inscrita', sender = 'MiTienda.com', recipients = [correo])
    msg.body = "Estimado " + str(nombre) + " " + str(apellido) + " su tienda " + str(tienda) + " ha sido registrada. En 24 horas le llegara un mensaje de activación de cuenta.  No responder este correo."
    mail.send(msg)

    