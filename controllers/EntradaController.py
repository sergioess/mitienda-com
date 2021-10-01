from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from werkzeug import datastructures

from models.entrada import Entrada
from models.producto import Producto
from datetime import datetime

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

@login_required
def index():
    entradasLista = Entrada.get_all()
    productosLista = Producto.get_all_activo()
    #print(type(entradasLista))

    #for entrada in entradasLista:
        #print('' + str(entrada.id_entradas) + ' ' + str(entrada.precio))

    return render_template('/entrada/index.html', entradas=entradasLista, productos=productosLista)

#@login_required
def store():
    _id_producto = request.form.get('txtProducto')
    _cantidad = request.form.get('txtCantidad')
    _precio = request.form.get('txtPrecio')
    _fecha_vencimiento = request.form.get('txtFecha_Ven')
    _proveedor = request.form.get('txtProveedor')
    date = datetime.now()

    nuevaEntrada = Entrada(_id_producto, _precio, date, _fecha_vencimiento, _cantidad, _proveedor)
    print (nuevaEntrada)
    nuevaEntrada.save()
    return redirect('/entrada')
    
def show():
    pass

#@login_required
def update():
    _id = request.form.get('txtId')
    _id_producto = request.form.get('txtProducto')
    _precio = request.form.get('txtPrecio')
    _fecha = request.form.get('txtFecha')
    _fecha_vencimiento = request.form.get('txtFecha_Ven')
    _cantidad = request.form.get('txtCantidad')
    _proveedor = request.form.get('txtProveedor')
    entrada = Entrada(_id_producto,_precio,_fecha,_fecha_vencimiento,_cantidad,_proveedor)
    print(entrada)
    entrada.update(_id)
    return redirect('/entrada')


def destroy(entrada_id):
    print(entrada_id)
    entrada = Entrada(entrada_id, 0, "13/12/2021", "13/12/2021", 0, "eliminar")
    print(entrada)
    entrada.delete()
    # entrada.activo = 0
    # entrada.save()
    return redirect('/entrada')
    
def create():
    pass
