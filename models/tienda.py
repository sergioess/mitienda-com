from datetime import date
from app import database


class Tienda(database.Model):

    __tablename__ = 'tiendas'

    id = database.Column(database.Integer, primary_key=True)
    nombre_tienda = database.Column(database.String, nullable=False)
    nit = database.Column(database.String, nullable=True)
    direccion = database.Column(database.String(100), nullable=False)
    telefono = database.Column(database.String(50), nullable=True)
    nombre_propietario = database.Column(database.String(100), nullable=False)
    ciudad= database.Column(database.String(60), nullable=True)

    @staticmethod
    def get_all():
        return Tienda.query.all()


    def get_by_id(id):
        return Tienda.query.filter_by(id=id).firts       
