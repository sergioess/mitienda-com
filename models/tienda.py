from datetime import date
from app import database
from sqlalchemy import asc, desc


class Tienda(database.Model):

    __tablename__ = 'tiendas'

    id = database.Column(database.Integer, primary_key=True)
    nombre_tienda = database.Column(database.String, nullable=False)
    nit = database.Column(database.String, nullable=True)
    direccion = database.Column(database.String(100), nullable=False)
    telefono = database.Column(database.String(50), nullable=True)
    nombre_propietario = database.Column(database.String(100), nullable=False)
    ciudad= database.Column(database.String(60), nullable=True)
    
    def __init__(self, nombre_tienda, nit, direccion, telefono, nombre_propietario, ciudad):
        self.nombre_tienda = nombre_tienda
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.nombre_propietario = nombre_propietario
        self.ciudad = ciudad

    @staticmethod
    def get_all():
        return Tienda.query.order_by(asc(Tienda.id)).all()  


    def get_by_id(id):
        return Tienda.query.filter_by(id=id).firts 

    def save(self):
        if not self.id:
            database.session.add(self)
        database.session.commit() 
        return self.id
            
    def update(self, id):
        tiendaActualiza = Tienda.query.filter_by(id=id).first()
        tiendaActualiza.nit = self.nit
        tiendaActualiza.telefono = self.telefono
        database.session.commit()
        return tiendaActualiza