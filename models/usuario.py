
from app import database


class Usuario(database.Model):

    __tablename__ = 'usuarios'

    id_usuario = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(50), nullable=False)
    apellidos = database.Column(database.String(50), nullable=False)
    correo = database.Column(database.String(50), nullable=False)
    nombre_usuario = database.Column(database.String(20), nullable=False)
    password = database.Column(database.String(20), nullable=False)
    #id_tienda = database.Column(database.Integer, nullable=False)
    activo = database.Column(database.Integer, nullable=False)
    rol = database.Column(database.String(30), nullable=False)

    @staticmethod
    def get_all():
        return Usuario.query.all()


    def get_by_id(id):
        return Usuario.query.filter_by(id=id).firts       
