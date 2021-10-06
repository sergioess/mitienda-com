
from app import database
from sqlalchemy import asc, desc
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


class Usuario(UserMixin,database.Model):

    __tablename__ = 'usuarios'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(50), nullable=False)
    apellidos = database.Column(database.String(50), nullable=False)
    correo = database.Column(database.String(50), unique=True, nullable=False)
    nombre_usuario = database.Column(database.String(20), unique=True, nullable=False)
    password = database.Column(database.String(20), nullable=False)
    id_tienda = database.Column(database.Integer, nullable=False)
    activo = database.Column(database.Integer, nullable=False)
    rol = database.Column(database.String(30), nullable=False)
    is_active = database.Column(database.Boolean, nullable=True, default=True)

    # rolid = database.Column(database.Integer, database.ForeignKey(rol.id))

#este es el toString personalizado
    def __str__(self):
        return f"<Usuario {self.id} {self.nombre} {self.apellidos} {self.correo} {self.nombre_usuario} {self.password} {self.id_tienda} {self.activo} {self.rol} >"

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
        return Usuario.query.all()

    @staticmethod
    def count_records():
        return Usuario.query.count()   

    @staticmethod
    def count_records_inacticos():
        return Usuario.query.filter_by(is_active=False).count()             

    @staticmethod
    def get_all_activo():
        return Usuario.query.filter_by(activo=1).order_by(asc(Usuario.id))   

    def get_by_id(id):
        return Usuario.query.filter_by(id=id).first()
    
    def save(self):
        if not self.id:
            usuario_existente = Usuario.query.filter_by(nombre_usuario=self.nombre_usuario).first()
            #print(usuario_existente.nombre)
            if usuario_existente is not None:
                print("Usuario ya existe en la base de datos")
                return False
            else:
                print("Usuario nuevo")
                self.is_active=False
                database.session.add(self)
                database.session.commit()
                return True


    def update(self):
        usuarioActualiza = Usuario.query.filter_by(id=self.id).first()
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
        usuarioActualiza = Usuario.query.filter_by(id=self.id).first()
        #print(categoriaActualiza)
        usuarioActualiza.activo = 0
        database.session.commit()
        return 1    

        
    @staticmethod
    def activar(id):
        usuarioActualiza = Usuario.query.filter_by(id=id).first()
        usuarioActualiza.is_active = True
        database.session.commit()
