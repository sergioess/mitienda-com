from flask import Flask

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.tienda import Tienda

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# app = Flask(__name__)
# app.config.from_object('config')

@login_required
def index():
    tiendasLista = Tienda.get_all()
 
    return render_template('/tienda/index.html', tiendas=tiendasLista)
  

def store():
    _id = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    tienda = Tienda(_id,_nombre )
    tienda.activo = 1
    tienda.id_tienda = 1
    tienda.save(tienda)
    return redirect('/tienda')
    
def show():
    pass


def update():
    _id = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    tienda = Tienda(_id,_nombre )
    Tienda.update(tienda)
    return redirect('/tienda')


def destroy(tienda_id):
    
    tienda = Tienda(tienda_id,'Elimina' )
    Tienda.delete(tienda)
    return redirect('/tienda')
    
def create():
    pass
