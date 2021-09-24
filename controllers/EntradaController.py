from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify

from models.entrada import Entrada

def index():
    entradasLista = Entrada.get_all()
    
    print(type(entradasLista))

    for entrada in entradasLista:
        print('' + str(entrada.id_entradas) + ' ' + str(entrada.precio))

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
