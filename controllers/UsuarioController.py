from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify

from models.usuario import Usuario

def index():
    usuariosLista = Usuario.get_all()
    
    print(type(usuariosLista))

    for usuario in usuariosLista:
        print('' + str(usuario.id_usuario) + ' ' + usuario.nombre)

    return "Hi everyone my friends"

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
