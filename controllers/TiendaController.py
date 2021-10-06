from flask import Flask, session

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.tienda import Tienda
from models.usuario import Usuario

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# app = Flask(__name__)
# app.config.from_object('config')

@login_required
def index():
    user = Usuario.query.filter_by(id=current_user.id).first()
    if(user.rol!="Administrador"):
        session.pop('_flashes', None)
        flash(f'Acceso no autorizado', 'danger')
        return redirect('/home')       
 
    tiendasLista = Tienda.get_all_activo()
    return render_template('/tienda/index.html', tiendas=tiendasLista)
  

def store():
    nombre_tienda = request.form.get('txtTienda')
    nit = request.form.get('txtNit')
    direccion = request.form.get('txtDireccion')
    telefono = request.form.get('txtTelefono')
    propietario = request.form.get('txtPropietario')
    ciudad = request.form.get('txtCiudad')
    nuevaTienda = Tienda(nombre_tienda, nit, direccion, telefono, propietario, ciudad)
    Tienda.save(nuevaTienda)
    return redirect('/tienda')
    
def show():
    pass


def update():
    _id = request.form.get('txtId')
    nombre_tienda = request.form.get('txtNmbre_tienda')
    nit = request.form.get('txtNit')
    direccion = request.form.get('txtDireccion')
    telefono = request.form.get('txtTelefono')
    propietario = request.form.get('txtPropietario')
    ciudad = request.form.get('txtCiudad')
    nuevaTienda = Tienda(nombre_tienda, nit, direccion, telefono, propietario, ciudad)
    nuevaTienda.update(_id)
    return redirect('/tienda')


def destroy(tienda_id):
    Tienda.delete(tienda_id)
    return redirect('/tienda')
    
def create():
    
    pass



