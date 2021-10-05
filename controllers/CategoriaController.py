from flask import Flask

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.categoria import Categoria
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# app = Flask(__name__)
# app.config.from_object('config')

@login_required
def index():
    categoriasLista = Categoria.get_all_activo()
    
    # print(type(categoriasLista))

    # for categoria in categoriasLista:
    #     print('' + str(categoria.id) + ' ' + categoria.nombre)

    # print(app.config['SQLALCHEMY_DATABASE_URI'])
    # return "Hola1"
    return render_template('/categoria/index.html', categorias=categoriasLista)
  
@login_required
def store():
    _id = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    categoria = Categoria(_id,_nombre )
    categoria.activo = 1
    categoria.id_tienda = current_user.id_tienda
    Categoria.save(categoria)
    return redirect('/categoria')
    
def show():
    pass

@login_required
def update():
    _id = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    categoria = Categoria(_id,_nombre )
    Categoria.update(categoria)
    return redirect('/categoria')

# @login_required
def destroy(categoria_id):
    
    categoria = Categoria(categoria_id,'Elimina' )
    Categoria.delete(categoria)
    # categoria.activo = 0
    # categoria.save()
    return redirect('/categoria')
    
def create():
    pass
