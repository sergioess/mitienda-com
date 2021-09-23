from datetime import date
from app import database


class Entrada(database.Model):

    __tablename__ = 'entradas'

    id_entradas = database.Column(database.Integer, primary_key=True)
    precio = database.Column(database.Float, nullable=False)
    #date = database.Column(database.date, nullable=False)
    id_producto = database.Column(database.Integer, nullable=False)
    #fecha_vencimiento = database.Column(database.date, nullable=True)
    cantidad = database.Column(database.Float, nullable=False)
    proveedor = database.Column(database.String, nullable=True)
    id_tienda= database.Column(database.Integer, nullable=False)
    total = database.Column(database.Float, nullable=False)

    @staticmethod
    def get_all():
        return Entrada.query.all()


    def get_by_id(id):
        return Entrada.query.filter_by(id=id).firts       
