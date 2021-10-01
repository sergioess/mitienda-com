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
    tiendasLista = Tienda.get_all()

    user = Usuario.query.filter_by(id=current_user.id).first()
    if(user.rol!="Administrador"):
        session.pop('_flashes', None)
        flash(f'Ruta no autorizada', 'danger')
        return redirect('/home')       
 
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
    nit = request.form.get('txtNit')
    telefono = request.form.get('txtTelefono')

    nuevaTienda = Tienda("nombre", nit, "direccion", telefono, "propietario", "ciudad")
    nuevaTienda.update(_id)
    return redirect('/tienda')


def destroy(tienda_id):
    
    tienda = Tienda(tienda_id,'Elimina')
    Tienda.delete(tienda)
    return redirect('/tienda')
    
def create():
    
    pass



