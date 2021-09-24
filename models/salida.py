from datetime import date
from app import database


class Salida(database.Model):

    __tablename__ = 'salidas'

    id_salidas = database.Column(database.Integer, primary_key=True)
    precio_unit = database.Column(database.Float, nullable=False)
    fecha = database.Column(database.Date, nullable=False)
    id_producto = database.Column(database.Integer, nullable=False)
    cantidad = database.Column(database.Float, nullable=False)
    precio_total = database.Column(database.Float, nullable=False)
    id_tienda= database.Column(database.Integer, nullable=False)

    @staticmethod
    def get_all():
        return Salida.query.all()


    def get_by_id(id):
        return Salida.query.filter_by(id=id).firts       
