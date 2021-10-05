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
    
    activo = database.Column(database.Integer)

    def __init__(self, nombre_tienda, nit, direccion, telefono, nombre_propietario, ciudad):
        self.nombre_tienda = nombre_tienda
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.nombre_propietario = nombre_propietario
        self.ciudad = ciudad

    def __init__(self, id):
        self.id = id

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

    @staticmethod
    def get_all_activo():
        return Tienda.query.filter_by(activo=1).order_by(asc(Tienda.id)).all()

    def get_by_id(id):
        return Tienda.query.filter_by(id=id).firts 

    def save(self):
        if not self.id:
            database.session.add(self)
        database.session.commit() 
        return self.id
    
    def update(self, id):
        tiendaActualiza = Tienda.query.filter_by(id=id).first()
        tiendaActualiza.nombre_tienda = self.nombre_tienda
        tiendaActualiza.nit = self.nit
        tiendaActualiza.direccion = self.direccion
        tiendaActualiza.telefono = self.telefono
        tiendaActualiza.nombre_propietario = self.nombre_propietario
        tiendaActualiza.ciudad = self.ciudad
        database.session.commit()
        return tiendaActualiza

    @staticmethod
    def delete(tienda_id):
        #print(self.id)
        tiendaActualiza = Tienda.query.filter_by(id=tienda_id).first()
        #print(categoriaActualiza)
        tiendaActualiza.activo = 0
        database.session.commit()
        
            
    def update(self, id):
        tiendaActualiza = Tienda.query.filter_by(id=id).first()
        tiendaActualiza.nit = self.nit
        tiendaActualiza.telefono = self.telefono
        database.session.commit()
        return tiendaActualiza