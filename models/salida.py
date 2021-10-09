from datetime import date
from app import database
from models.producto import Producto
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import asc, desc

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

class Salida(database.Model):

    __tablename__ = 'salidas'

    id_salidas = database.Column(database.Integer, primary_key=True)
    precio_unit = database.Column(database.Float, nullable=False)
    fecha = database.Column(database.Date, nullable=False)
    cantidad = database.Column(database.Float, nullable=False)
    precio_total = database.Column(database.Float, nullable=False)
    id_tienda= database.Column(database.Integer, nullable=False)
    id_producto = database.Column(database.Integer, ForeignKey("productos.id"))
    
    producto_salida = database.relationship("Producto", backref='productos.id', lazy='joined')

    def __init__(self, id_producto, precio_unit, fecha, cantidad):
        self.id_producto = id_producto
        self.precio_unit = precio_unit
        self.fecha = fecha
        self.cantidad = cantidad



    def __str__(self):
        return f"<Salida {self.id_salidas} {self.precio_unit} {self.fecha} {self.cantidad} {self.id_producto} >"        

    @staticmethod
    def get_all():
        salidas = database.session.query(Salida,Producto).join(Producto).filter(Salida.id_tienda==current_user.id_tienda).order_by(asc(Salida.id_salidas)).all()
        # sergios = Salida.query.all()

        # for sergio in salidas:
        #     print(sergio)
        #     print(sergio.Salida.id_salidas, sergio.Producto.nombre)
        return salidas
        # return database.query(Salida).join(Producto).all()


    def get_by_id(id):
        return Salida.query.filter_by(id=id).first()       


    def get_by_id(id):
        return Salida.query.filter_by(id_salidas=id).first()    

    # @staticmethod
    def update(self, id):
        nuevaCantidad = self.cantidad
        salidaActualiza = Salida.query.filter_by(id_salidas=id).first()
        # print(salidaActualiza)
        antiguaCantidad = salidaActualiza.cantidad
        salidaActualiza.precio_unit = self.precio_unit
        salidaActualiza.cantidad = self.cantidad
        salidaActualiza.precio_total = float(self.cantidad) * float(self.precio_unit)
        
        database.session.commit()
        # print(nuevaCantidad)
        # print(salidaActualiza.cantidad)
        # resta lo que hay actual 
        prorductoActualiza = Producto.query.filter_by(id=salidaActualiza.id_producto).first()
        prorductoActualiza.stock = float(prorductoActualiza.stock) + float(antiguaCantidad)
        database.session.commit()


        prorductoActualiza.stock = float(prorductoActualiza.stock) - float(nuevaCantidad)
        database.session.commit()

        return salidaActualiza

    @staticmethod
    def delete(id):
        # print(self.id_producto)
        salidaActualiza = Salida.query.filter_by(id_salidas=id).first()
        #print(salidaActualiza)
        database.session.delete(salidaActualiza)
        database.session.commit()
        
        prorductoActualiza = Producto.query.filter_by(id=salidaActualiza.id_producto).first()
        prorductoActualiza.stock = prorductoActualiza.stock + salidaActualiza.cantidad
        database.session.commit()
        
   
    def save(self):
        prorductoActualiza = Producto.query.filter_by(id=self.id_producto).first()
        if float (prorductoActualiza.stock) >= float(self.cantidad) :

            self.precio_total = float(self.cantidad) * float(self.precio_unit)
            self.id_tienda = current_user.id_tienda
            #print (self)
            database.session.add(self)
            database.session.commit()
            # print(self.id_producto)
            prorductoActualiza = Producto.query.filter_by(id=self.id_producto).first()
            prorductoActualiza.stock = prorductoActualiza.stock - self.cantidad
            database.session.commit()
            # print(prorductoActualiza)
            return True 
        else:
            return False


