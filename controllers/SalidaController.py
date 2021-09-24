from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify

from models.salida import Salida

def index():
    salidasLista = Salida.get_all()
    
    print(type(salidasLista))

    for salida in salidasLista:
        print('' + str(salida.id_salidas) + ' ' + str(salida.precio_unit))

    return "Hi everyone"

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
