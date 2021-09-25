
from app import database
from sqlalchemy import asc, desc


class Usuario(database.Model):

    __tablename__ = 'usuarios'

    id_usuario = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(50), nullable=False)
    apellidos = database.Column(database.String(50), nullable=False)
    correo = database.Column(database.String(50), nullable=False)
    nombre_usuario = database.Column(database.String(20), nullable=False)
    password = database.Column(database.String(20), nullable=False)
    id_tienda = database.Column(database.Integer, nullable=False)
    activo = database.Column(database.Integer, nullable=False)
    rol = database.Column(database.String(30), nullable=False)

    # rolid = database.Column(database.Integer, database.ForeignKey(rol.id))

#este es el toString personalizado
    def __str__(self):
        return f"<Usuario {self.id_usuario} {self.nombre} {self.apellidos} {self.correo} {self.nombre_usuario} {self.password} {self.id_tienda} {self.activo} {self.rol} >"

    def __init__(self, id):
            self.id_usuario = id

    def __init__(self, id, nombre, apellidos, correo, nombre_usuario, password, rol):
        self.id_usuario = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.nombre_usuario = nombre_usuario
        self.password = password
        #self.activo = activo
        self.rol = rol


    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def count_records():
        return Usuario.query.count()      

    @staticmethod
    def get_all_activo():
        return Usuario.query.filter_by(activo=1).order_by(asc(Usuario.id_usuario))   

    def get_by_id(id):
        return Usuario.query.filter_by(id_usuario=id).firts
    
    def save(self):
        if not self.id_usuario:
            database.session.add(self)
        database.session.commit()


    def update(self):
        usuarioActualiza = Usuario.query.filter_by(id_usuario=self.id_usuario).first()
        usuarioActualiza.nombre = self.nombre
        usuarioActualiza.apellidos = self.apellidos
        usuarioActualiza.correo = self.correo
        usuarioActualiza.nombre_usuario = self.nombre_usuario
        usuarioActualiza.password = self.password
        usuarioActualiza.rol = self.rol
        database.session.commit()
        return usuarioActualiza

    def delete(self):
        #print(self.id)
        usuarioActualiza = Usuario.query.filter_by(id_usuario=self.id_usuario).first()
        #print(categoriaActualiza)
        usuarioActualiza.activo = 0
        database.session.commit()
        return 1    
