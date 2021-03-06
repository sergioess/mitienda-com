from datetime import date
from app import database
from models.producto import Producto
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import asc, desc

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user



class Entrada(database.Model):

    __tablename__ = 'entradas'

    id_entradas = database.Column(database.Integer, primary_key=True)
    precio = database.Column(database.Float, nullable=False)
    fecha = database.Column(database.Date, nullable=False)
    id_producto = database.Column(database.Integer, ForeignKey("productos.id"))
    fecha_vencimiento = database.Column(database.Date, nullable=True)
    cantidad = database.Column(database.Float, nullable=False)
    proveedor = database.Column(database.String, nullable=True)
    id_tienda= database.Column(database.Integer, nullable=False)
    total = database.Column(database.Float, nullable=False)
   
    
    producto_entrada = database.relationship("Producto", backref='productos.nombre', lazy='joined')  
    
    def __str__(self):
        return f"<Entrada {self.id_entradas} {self.precio} {self.proveedor} {self.cantidad} >"

    


    def __init__(self, id_producto, precio, fecha, fecha_vencimento, cantidad, proveedor):
        self.id_producto = id_producto
        self.precio = precio
        self.fecha = fecha
        self.fecha_vencimiento = fecha_vencimento
        self.cantidad = cantidad
        self.proveedor = proveedor

    #def __init__(self, id_entradas, proveedor):
        #self.id_entradas = id_entradas
        #self.proveedor = proveedor



    @staticmethod
    def get_all():
        entradas = database.session.query(Entrada,Producto).join(Producto).filter(Entrada.id_tienda==current_user.id_tienda).order_by(asc(Entrada.id_entradas)).all()
        # sergios = Salida.query.all()

        # for sergio in salidas:
        #     print(sergio)
        #     print(sergio.Salida.id_salidas, sergio.Producto.nombre)
        return entradas
        # return database.query(Salida).join(Producto).all()



    def get_by_id(id):
        return Entrada.query.filter_by(id_entradas=id).firts    



    def update(self, id):
        nuevaCantidad = self.cantidad
        entradaActualiza = Entrada.query.filter_by(id_entradas=id).first()
        # print(entradaActualiza)
        antiguaCantidad = entradaActualiza.cantidad
        entradaActualiza.total = float(self.cantidad) * float(self.precio)
        entradaActualiza.precio = self.precio
        entradaActualiza.fecha = self.fecha
        entradaActualiza.fecha_vencimiento = self.fecha_vencimiento
        entradaActualiza.cantidad = self.cantidad
        entradaActualiza.proveedor = self.proveedor
        database.session.commit()

        prorductoActualiza = Producto.query.filter_by(id=entradaActualiza.id_producto).first()
        prorductoActualiza.stock = float(prorductoActualiza.stock) - float(antiguaCantidad)
        database.session.commit()


        prorductoActualiza.stock = float(prorductoActualiza.stock) + float(nuevaCantidad)
        database.session.commit()

        return entradaActualiza

    def delete(self):
        print(self.id_producto)
        entradaActualiza = Entrada.query.filter_by(id_entradas=self.id_producto).first()
        # print(entradaActualiza)

        database.session.delete(entradaActualiza)
        database.session.commit()

        prorductoActualiza = Producto.query.filter_by(id=entradaActualiza.id_producto).first()
        prorductoActualiza.stock = prorductoActualiza.stock - entradaActualiza.cantidad
        database.session.commit()
        

    def save(self):
        self.total = float(self.cantidad) * float(self.precio)
        self.id_tienda = current_user.id_tienda
        print (self)
        database.session.add(self)
        database.session.commit()
        
        prorductoActualiza = Producto.query.filter_by(id=self.id_producto).first()
        prorductoActualiza.stock = prorductoActualiza.stock + self.cantidad
        database.session.commit()


