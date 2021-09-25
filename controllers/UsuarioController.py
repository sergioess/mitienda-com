from flask import Flask

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.usuario import Usuario

def index():
    usuariosLista = Usuario.get_all_activo()
    
    #print(type(usuariosLista))

    #for usuario in usuariosLista:
    #    print('' + str(usuario.id_usuario) + ' ' + usuario.nombre)
    #    print(usuario)
    return render_template('/usuario/index.html', usuarios=usuariosLista)

def store():
    _id_usuario = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    _apellidos = request.form.get('txtApellidos')
    _correo = request.form.get('txtCorreo')
    _nombre_usuario = request.form.get('txtNombre_usuario')
    _password = request.form.get('txtPassword')
    _rol = request.form.get('txtRol')
    usuario = Usuario(_id_usuario,_nombre, _apellidos, _correo, _nombre_usuario, _password, _rol)
    usuario.activo = 1
    usuario.id_tienda = 1
    Usuario.save(usuario)
    return redirect('/usuario')

    
def show():
    pass

def update():
    _id_usuario = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    _apellidos = request.form.get('txtApellidos')
    _correo = request.form.get('txtCorreo')
    _nombre_usuario = request.form.get('txtNombre_usuario')
    _password = request.form.get('txtPassword')
    _rol = request.form.get('txtRol')
    usuario = Usuario(_id_usuario, _nombre, _apellidos, _correo, _nombre_usuario, _password, _rol)
    Usuario.update(usuario)
    return redirect('/usuario')


def destroy(usuario_id_usuario):
    usuario = Usuario(usuario_id_usuario, "Cesar", "Mendoza", "cesar@correo.com", "c24mendoza", "1234", "Tendero")
    Usuario.delete(usuario)
    # usuario.activo = 0
    # usuario.save()
    return redirect('/usuario')
    
def create():
    pass
