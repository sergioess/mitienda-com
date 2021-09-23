from flask import Flask

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify

from models.categoria import Categoria

# app = Flask(__name__)
# app.config.from_object('config')

def index():
    categoriasLista = Categoria.get_all()
    
    print(type(categoriasLista))

    for categoria in categoriasLista:
        print('' + str(categoria.id) + ' ' + categoria.nombre)

    # print(app.config['SQLALCHEMY_DATABASE_URI'])
    return "Hola1"

def store():
    pass
    
def show():
    pass

def update():
    pass

def destroy():
    pass
    
def create():
    pass
