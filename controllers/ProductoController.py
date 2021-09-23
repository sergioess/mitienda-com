from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify

from models.producto import Producto

def index():
    productosLista = Producto.get_all()
    
    print(type(productosLista))

    for producto in productosLista:
        print('' + str(producto.id) + ' ' + producto.nombre)

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
