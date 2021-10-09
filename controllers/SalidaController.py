from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from werkzeug import datastructures

from models.salida import Salida
from models.producto import Producto
from datetime import datetime

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

@login_required
def index():
    salidasLista = Salida.get_all()
    productosLista = Producto.get_all_activo()
    return render_template('/salida/index.html', salidas=salidasLista, productos=productosLista)

# @login_required
def store():
    _id_producto = request.form.get('txtProducto')
    if (int(_id_producto) >= 1 ):
        _cantidad = request.form.get('txtCantidad')
        _precio = request.form.get('txtPrecio')
        date = datetime.now()
          
        nuevaSalida = Salida(_id_producto, _precio, date, _cantidad)
        #print (nuevaSalida)
        if nuevaSalida.save():
            return redirect('/salida') 
        
        else:
            flash(f'Stock de producto insuficiente', 'danger')
            return redirect('/salida')
            



    
    
def show():
    pass

# @login_required
def update():
    _id = request.form.get('txtId')
    _idproducto = request.form.get('txtIdProducto')
    _precio_unit = request.form.get('txtPrecio')
    _fecha = request.form.get('txtFecha')
    _cantidad = request.form.get('txtCantidad')
    salida = Salida(_idproducto,_precio_unit,_fecha,_cantidad)
    #print("Id Salida -> ", _id)
    #print("Id Producto -> ", _idproducto)
    #print(salida)
    salida.update(_id)
    return redirect('/salida')

# @login_required
def destroy(salida_id):
    #print(salida_id)
    Salida.delete(salida_id)
    return redirect('/salida')
    
def create():
    pass

