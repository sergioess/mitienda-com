from app import database


class Rol(database.Model):
    __tablename__ = 'rol'
    
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(50), nullable=False)
    descripcion = database.Column(database.String(50), nullable=True)

    # relationships
    usuarios = relationship('Usuario', backref='Usuario.id',primaryjoin='Usuario.id==Rol.id', lazy='dynamic')