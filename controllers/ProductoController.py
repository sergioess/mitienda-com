from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from models.categoria import Categoria
from models.producto import Producto

# con este se listan los productos
def index():
    productosLista = Producto.get_all_activo()
    categorias = Categoria.get_all_activo()
    return render_template('/producto/index.html', productos=productosLista, categorias=categorias)

#con este método se almacena un nuevo registro
def store():
    _nombre = request.form.get('txtNombre')
    _referencia = request.form.get('txtReferencia')
    _costo = request.form.get('txtCosto')
    _precio_venta = request.form.get('txtPrecio_venta') 
    _categoria = request.form.get('txtCategoria')    
    producto = Producto(_nombre, _referencia, _costo, _precio_venta, 1, 0, _categoria )
    print(producto)
    Producto.save(producto)
    return redirect('/producto')
    
def show():
    pass

# con este método se actualiza un registro
def update():
    _id = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    _referencia = request.form.get('txtReferencia')
    _costo = request.form.get('txtCosto')
    _precio_venta = request.form.get('txtPrecio_venta')
    producto = Producto(_nombre, _referencia, _costo, _precio_venta,1,0 )
    producto.update(_id)
    return redirect('/producto')

# con este método se elimina un registro
def destroy(producto_id):
    Producto.delete(producto_id)
    return redirect('/producto')
    
def create():
    pass
    

