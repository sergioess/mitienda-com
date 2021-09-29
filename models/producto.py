from app import database
from sqlalchemy import asc, desc
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.categoria import Categoria
from sqlalchemy import asc, desc

class Producto(database.Model):

    __tablename__ = 'productos'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    referencia = database.Column(database.String, nullable=False)
    costo = database.Column(database.Float, nullable=False)
    precio_venta = database.Column(database.Float, nullable=False)
    imagen = database.Column(database.String, nullable=True)
    tienda_id = database.Column(database.Integer)
    activo = database.Column(database.Integer, nullable=False)
    stock = database.Column(database.Float, nullable=False)
    categoria_id = database.Column(database.Integer, ForeignKey("categorias.id"))
    
    categoria_producto = database.relationship("Categoria", backref='categorias.nombre', lazy='joined')

    # este es el constructor de la clase
    def __init__(self, nombre: str, referencia: str, costo, precio_venta, activo: int, stock, categoria_id, imagen):
        self.nombre = nombre
        self.referencia = referencia
        self.costo = costo
        self.precio_venta = precio_venta
        self.activo = activo
        self.stock = stock
        self.categoria_id = categoria_id
        self.imagen = imagen

    # método to string  (de python)
    def __str__(self):
        return f"<Producto {self.id} {self.nombre} {self.referencia} {self.costo} {self.precio_venta} {self.activo} {self.stock} {self.categoria_id} >"

    @staticmethod
    def get_all():
        productos = database.session.query(Producto, Categoria).join(Categoria).order_by(asc(Producto.id)).all()
        return productos

    # con este obtenemos toda la info que hay
    # @staticmethod
    # def get_all():
    #     return Producto.query.all()

    # con este se filtra la información para hacer una búsqueda
    @staticmethod
    def get_all_activo():
        #return Producto.query.filter_by(activo=1).order_by(asc(Producto.id))
        productos = database.session.query(Producto, Categoria).join(Categoria).filter(Producto.activo==1).order_by(asc(Producto.id)).all()

        return productos

    # con este se hace un conteo de productos
    @staticmethod
    def count_records():
        return Producto.query.count()

    # Con este actualiza un registro, son llamados por el controlador
    def update(self, id):
        productoActualiza = Producto.query.filter_by(id=id).first()
        productoActualiza.nombre = self.nombre
        productoActualiza.referencia = self.referencia
        productoActualiza.costo = self.costo
        productoActualiza.precio_venta = self.precio_venta
        productoActualiza.imagen = self.imagen
        database.session.commit()
        return productoActualiza

    # con este se inactiva un registro
    @staticmethod
    def delete(id):
        # print(self.id)
        productoActualiza = Producto.query.filter_by(id=id).first()
        # print(productoActualiza)
        productoActualiza.activo = 0
        database.session.commit()
        return 0

    # este es para guardar un nuevo registro
    def save(self):
        self.tienda_id = 1
        print(self)
        database.session.add(self)
        database.session.commit()

    #con este se filtra para obtener una búsqueda
    def get_by_id(id):
        return Producto.query.filter_by(id=id).firts
