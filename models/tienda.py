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
    
    def __init__(self, nombre_tienda, nit, direccion, telefono, nombre_propietario, ciudad):
        self.nombre_tienda = nombre_tienda
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.nombre_propietario = nombre_propietario
        self.ciudad = ciudad

    def __init__(self, id):
        self.id = id

    def __init__(self, id, nombre_tienda, nit, direccion, telefono, nombre_propietario, ciudad):
        self.id = id
        self.nombre_tienda = nombre_tienda
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.nombre_propietario = nombre_propietario
        self.ciudad = ciudad

    @staticmethod
    def get_all():
        return Tienda.query.all()


    def get_by_id(id):
        return Tienda.query.filter_by(id=id).firts 

    def save(self):
        if not self.id:
            database.session.add(self)
        database.session.commit() 
        return self.id
    
    def update(self):
        tiendaActualiza = Tienda.query.filter_by(id=self.id).first()
        tiendaActualiza.nombre_tienda = self.nombre_tienda
        tiendaActualiza.nit = self.nit
        tiendaActualiza.direccion = self.direccion
        tiendaActualiza.telefono = self.telefono
        tiendaActualiza.nombre_propietario = self.nombre_propietario
        tiendaActualiza.ciudad = self.ciudad
        database.session.commit()
        return tiendaActualiza

    def delete(self):
        #print(self.id)
        tiendaActualiza = Tienda.query.filter_by(id=self.id).first()
        #print(categoriaActualiza)
        tiendaActualiza.activo = 0
        database.session.commit()
        return 1
            
