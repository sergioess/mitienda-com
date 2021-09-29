
from app import database
from sqlalchemy import asc, desc
from app import Bcrypt ,bcrypt


class User(database.Model):

    __tablename__ = 'usuarios'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(50), nullable=False)
    apellidos = database.Column(database.String(50), nullable=False)
    correo = database.Column(database.String(50), nullable=False)
    nombre_usuario = database.Column(database.String(20), nullable=False)
    password = database.Column(database.String(80), nullable=False)
    id_tienda = database.Column(database.Integer, nullable=False)
    activo = database.Column(database.Integer, nullable=False)
    rol = database.Column(database.String(30), nullable=False)

    # rolid = database.Column(database.Integer, database.ForeignKey(rol.id))

#este es el toString personalizado
    def __str__(self):
        return f"<User {self.id} {self.nombre} {self.apellidos} {self.correo} {self.nombre_usuario} {self.password} {self.id_tienda} {self.activo} {self.rol} >"

    def __init__(self, id):
            self.id = id

    def __init__(self, id, nombre, apellidos, correo, nombre_usuario, password, rol):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.activo = 1
        self.rol = rol


    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def count_records():
        return User.query.count()      

    @staticmethod
    def get_all_activo():
        return User.query.filter_by(activo=1).order_by(asc(User.id))   

    def get_by_id(id):
        return User.query.filter_by(id=id).firts
    
    def save(self):
        if not self.id:
            database.session.add(self)
        database.session.commit()


    def update(self):
        UserActualiza = User.query.filter_by(id=self.id).first()
        UserActualiza.nombre = self.nombre
        UserActualiza.apellidos = self.apellidos
        UserActualiza.correo = self.correo
        UserActualiza.nombre_usuario = self.nombre_usuario
        UserActualiza.password = self.password
        UserActualiza.rol = self.rol
        database.session.commit()
        return UserActualiza

    def delete(self):
        #print(self.id)
        UserActualiza = User.query.filter_by(id=self.id).first()
        #print(categoriaActualiza)
        UserActualiza.activo = 0
        database.session.commit()
        return 1    
