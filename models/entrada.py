from datetime import date
from app import database


class Entrada(database.Model):

    __tablename__ = 'entradas'

    id_entradas = database.Column(database.Integer, primary_key=True)
    precio = database.Column(database.Float, nullable=False)
    fecha = database.Column(database.Date, nullable=False)
    id_producto = database.Column(database.Integer, nullable=False)
    fecha_vencimiento = database.Column(database.Date, nullable=True)
    cantidad = database.Column(database.Float, nullable=False)
    proveedor = database.Column(database.String, nullable=True)
    id_tienda= database.Column(database.Integer, nullable=False)
    total = database.Column(database.Float, nullable=False)

    def __str__(self):
        return f"<Entrada {self.id_entradas} {self.precio} {self.proveedor} {self.cantidad} >"

    


    def __init__(self, id_entradas, precio, fecha, fecha_vencimento, cantidad, proveedor):
        self.id_entradas = id_entradas
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
        return Entrada.query.all()


    def get_by_id(id):
        return Entrada.query.filter_by(id_entradas=id).firts    

    def update(self):
        entradaActualiza = Entrada.query.filter_by(id_entradas=self.id).first()
        entradaActualiza.nombre = self.precio
        entradaActualiza.nombre = self.fecha
        entradaActualiza.nombre = self.fecha_vencimiento
        entradaActualiza.nombre = self.cantidad
        entradaActualiza.nombre = self.proveedor
        database.session.commit()
        return entradaActualiza

    def delete(self):
        print(self.id_entradas)
        entradaActualiza = Entrada.query.filter_by(id_entradas=self.id_entradas).first()
        print(entradaActualiza)
        #entradaActualiza.activo = 0
        database.session.delete(entradaActualiza)
        database.session.commit()
        return 1  
