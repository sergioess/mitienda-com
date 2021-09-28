from flask import Flask

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.categoria import Categoria
from models.producto import Producto
from models.usuario import Usuario

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config.from_object('config')

@login_required
def home():
    categoriasTotal = Categoria.count_records()
    productosTotal = Producto.count_records()
    return render_template('/home.html', totalcategoria=categoriasTotal, totalproducto=productosTotal)

def index():
    return render_template('/index.html')

def frmlogin():
    return render_template('/login.html')    


@login_required
def logout():
    logout_user()
    return render_template('index.html') 
    #return 'You are now logged out!'    

def login():
    _nombre = request.form.get('txtNombre')
    print(_nombre)
    user = Usuario.query.filter_by(nombre_usuario=_nombre).first()
    print(user)
    login_user(user)
    return render_template('home.html') 
    #return 'You are now logged in!'       