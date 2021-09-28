from datetime import date
from app import database
from models.producto import Producto
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



class Entrada(database.Model):

    __tablename__ = 'entradas'

    id_entradas = database.Column(database.Integer, primary_key=True)
    precio = database.Column(database.Float, nullable=False)
    fecha = database.Column(database.Date, nullable=False)
    id_producto = database.Column(database.Integer, ForeignKey("productos.id"))
    #id_producto = database.Column(database.Integer, nullable=False)
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
        entradas = database.session.query(Entrada,Producto).join(Producto).all()
        # sergios = Salida.query.all()

        # for sergio in salidas:
        #     print(sergio)
        #     print(sergio.Salida.id_salidas, sergio.Producto.nombre)
        return entradas
        # return database.query(Salida).join(Producto).all()



    def get_by_id(id):
        return Entrada.query.filter_by(id_entradas=id).firts    



    def update(self, id):
        entradaActualiza = Entrada.query.filter_by(id_entradas=id).first()
        print(entradaActualiza)

        entradaActualiza.precio = self.precio
        entradaActualiza.fecha = self.fecha
        entradaActualiza.fecha_vencimiento = self.fecha_vencimiento
        entradaActualiza.cantidad = self.cantidad
        entradaActualiza.proveedor = self.proveedor
        database.session.commit()
        return entradaActualiza

    def delete(self):
        print(self.id_producto)
        entradaActualiza = Entrada.query.filter_by(id_entradas=self.id_producto).first()
        print(entradaActualiza)
        #entradaActualiza.activo = 0
        database.session.delete(entradaActualiza)
        database.session.commit()
        return 1  

    def save(self):
        self.total = float(self.cantidad) * float(self.precio)
        self.id_tienda = 1
        print (self)
        database.session.add(self)
        database.session.commit()


