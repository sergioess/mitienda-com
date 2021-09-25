
from app import database
from sqlalchemy import asc, desc


class Categoria(database.Model):

    __tablename__ = 'categorias'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    id_tienda = database.Column(database.Integer, nullable=False)
    activo = database.Column(database.Integer, nullable=False)
<<<<<<< HEAD
    # productos = database.relationship("producto", backref = "categoria", lazy = True)
=======
    #productos = database.relationship("producto", backref = "categoria", lazy = True)
>>>>>>> 5aecd7a2b36dbbd8f4e3afdc9292cfc20ceeb546
    #este es el toString personalizado
    def __str__(self):
        return f"<Categoria {self.id} {self.nombre} {self.id_tienda} {self.activo} >"

    def __init__(self, id):
        self.id = id



    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


    @staticmethod
    def get_all():
        return Categoria.query.all()

    @staticmethod
    def count_records():
        return Categoria.query.count()      

    @staticmethod
    def get_all_activo():
        return Categoria.query.filter_by(activo=1).order_by(asc(Categoria.id))   

    @staticmethod
    def get_by_id(self):
        
        return Categoria.query.filter_by(id=self.id).first    


    def save(self):
        if not self.id:
            database.session.add(self)
        database.session.commit()


    def update(self):
        categoriaActualiza = Categoria.query.filter_by(id=self.id).first()
        categoriaActualiza.nombre = self.nombre
        database.session.commit()
        return categoriaActualiza

    def delete(self):
        #print(self.id)
        categoriaActualiza = Categoria.query.filter_by(id=self.id).first()
        #print(categoriaActualiza)
        categoriaActualiza.activo = 0
        database.session.commit()
        return 1