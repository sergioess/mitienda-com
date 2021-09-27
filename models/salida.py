from datetime import date
from app import database
from models.producto import Producto
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Salida(database.Model):

    __tablename__ = 'salidas'

    id_salidas = database.Column(database.Integer, primary_key=True)
    precio_unit = database.Column(database.Float, nullable=False)
    fecha = database.Column(database.Date, nullable=False)
    cantidad = database.Column(database.Float, nullable=False)
    precio_total = database.Column(database.Float, nullable=False)
    id_tienda= database.Column(database.Integer, nullable=False)
    id_producto = database.Column(database.Integer, ForeignKey("productos.id"))
    
    producto_salida = database.relationship("Producto", backref='productos.nombre', lazy='joined')

    def __init__(self, id_producto, precio_unit, fecha, cantidad):
        self.id_producto = id_producto
        self.precio_unit = precio_unit
        self.fecha = fecha
        self.cantidad = cantidad



    def __str__(self):
        return f"<Entrada {self.id_salidas} {self.precio_unit} {self.fecha} {self.cantidad} {self.id_producto} >"        

    @staticmethod
    def get_all():
        salidas = database.session.query(Salida,Producto).join(Producto).all()
        # sergios = Salida.query.all()

        # for sergio in salidas:
        #     print(sergio)
        #     print(sergio.Salida.id_salidas, sergio.Producto.nombre)
        return salidas
        # return database.query(Salida).join(Producto).all()


    def get_by_id(id):
        return Salida.query.filter_by(id=id).firts       


    def get_by_id(id):
        return Salida.query.filter_by(id_salidas=id).firts    

    def update(self, id):
        nuevaCantidad = self.cantidad
        salidaActualiza = Salida.query.filter_by(id_salidas=id).first()
        # print(salidaActualiza)
        antiguaCantidad = salidaActualiza.cantidad
        salidaActualiza.precio_unit = self.precio_unit
        salidaActualiza.cantidad = self.cantidad
        salidaActualiza.precio_total = float(self.cantidad) * float(self.precio_unit)
        
        database.session.commit()
        print(nuevaCantidad)
        print(salidaActualiza.cantidad)
        # resta lo que hay actual 
        prorductoActualiza = Producto.query.filter_by(id=salidaActualiza.id_producto).first()
        prorductoActualiza.stock = float(prorductoActualiza.stock) + float(antiguaCantidad)
        database.session.commit()


        prorductoActualiza.stock = float(prorductoActualiza.stock) - float(nuevaCantidad)
        database.session.commit()

        return salidaActualiza

    def delete(self):
        # print(self.id_producto)
        salidaActualiza = Salida.query.filter_by(id_salidas=self.id_producto).first()
        print(salidaActualiza)
        database.session.delete(salidaActualiza)
        database.session.commit()
        
        prorductoActualiza = Producto.query.filter_by(id=salidaActualiza.id_producto).first()
        prorductoActualiza.stock = prorductoActualiza.stock + salidaActualiza.cantidad
        database.session.commit()
        

    def save(self):
        self.precio_total = float(self.cantidad) * float(self.precio_unit)
        self.id_tienda = 1
        #print (self)
        database.session.add(self)
        database.session.commit()
        # print(self.id_producto)
        prorductoActualiza = Producto.query.filter_by(id=self.id_producto).first()
        prorductoActualiza.stock = prorductoActualiza.stock - self.cantidad
        database.session.commit()
        # print(prorductoActualiza) 


