from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify

from models.producto import Producto

def index():
    productosLista = Producto.get_all()
    
    #print(type(productosLista))

    #for producto in productosLista:
        #print('' + str(producto.id) + ' ' + producto.nombre)
    return render_template('/producto/index.html', productos=productosLista)

def store():
    _nombre = request.form.get('txtNombre')
    _referencia = request.form.get('txtReferencia')
    _costo = request.form.get('txtCosto')
    _precio_venta = request.form.get('txtPrecio_venta')    
    producto = Producto(_nombre, _referencia, _costo, _precio_venta, 1, 0 )
    print(producto)
    Producto.save(producto)
    return redirect('/producto')
    
def show():
    pass

def update():
    _id = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    _referencia = request.form.get('txtReferencia')
    _costo = request.form.get('txtCosto')
    _precio_venta = request.form.get('txtPrecio_venta')
    producto = Producto(_id,_nombre, _referencia, _costo, _precio_venta )
    producto.update(producto)
    return redirect('/producto')


def destroy(producto_id):
    
    producto = Producto(producto_id,'Elimina' )
    producto.delete(producto)
    # producto.activo = 0
    # producto.save()
    return redirect('/producto')
    
def create():
    pass
    
def create():
    pass
