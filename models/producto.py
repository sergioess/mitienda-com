from app import database


class Producto(database.Model):

    __tablename__ = 'productos'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    referencia = database.Column(database.String, nullable=False)
    costo = database.Column(database.Float, nullable=False)
    precio_venta = database.Column(database.Float, nullable=False)
    imagen = database.Column(database.String, nullable=True)
    #id_tienda = database.Column(database.Integer, nullable=False)
    #id_categoria = database.Column(database.Integer, nullable=False)
    activo = database.Column(database.Integer, nullable=False)

    @staticmethod
    def get_all():
        return Producto.query.all()


    def get_by_id(id):
        return Producto.query.filter_by(id=id).firts       
