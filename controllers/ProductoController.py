from flask import Flask
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from models.categoria import Categoria
from models.producto import Producto
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import sys
import os
app = Flask(__name__)
app.config.from_object('config')


# con este se listan los productos
@login_required
def index():
    productosLista = Producto.get_all_activo()
    categorias = Categoria.get_all_activo()
    return render_template('/producto/index.html', productos=productosLista, categorias=categorias)

#con este método se almacena un nuevo registro
@login_required
def store():
    _nombre = request.form.get('txtNombre')
    _referencia = request.form.get('txtReferencia')
    _costo = request.form.get('txtCosto')
    _precio_venta = request.form.get('txtPrecio_venta') 
    _categoria = request.form.get('txtCategoria') 
    _foto=request.files.get('txtFoto')
		
    now=datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if(_foto.filename != ''):
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uplproductos/" + nuevoNombreFoto)

   
    producto = Producto(_nombre, _referencia, _costo, _precio_venta, current_user.id_tienda, 0, _categoria, nuevoNombreFoto )
    print(producto)
    producto.save()
    return redirect('/producto')
    
def show():
    pass

# con este método se actualiza un registro
@login_required
def update():
    _id = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    _referencia = request.form.get('txtReferencia')
    _costo = request.form.get('txtCosto')
    _precio_venta = request.form.get('txtPrecio_venta')
    _categoria = request.form.get('txtCategoria')
    _foto=request.files.get('txtFoto')
    now=datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    actualizaProducto = Producto.query.filter_by(id=_id).first()
    nuevoNombreFoto = actualizaProducto.imagen
    if(_foto.filename != ''):
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uplproductos/" + nuevoNombreFoto)
        
        if len(actualizaProducto.imagen) != 0   :
            os.remove(os.path.join(app.config['CARPETA_PTOS'], actualizaProducto.imagen))
    
    producto = Producto(_nombre, _referencia, _costo, _precio_venta,1,0, _categoria, nuevoNombreFoto )
    producto.update(_id)
    return redirect('/producto')

# con este método se elimina un registro
def destroy(producto_id):
    Producto.delete(producto_id)
    return redirect('/producto')
    
def create():
    pass
    

