from flask import Flask

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify

from models.categoria import Categoria



def index():
    categoriasLista = Categoria.get_all()
    
    print(type(categoriasLista))

    for categoria in categoriasLista:
        print('' + str(categoria.id) + ' ' + categoria.nombre)
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
