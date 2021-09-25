from app import database


class Producto(database.Model):

    __tablename__ = 'productos'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    referencia = database.Column(database.String, nullable=False)
    costo = database.Column(database.Float, nullable=False)
    precio_venta = database.Column(database.Float, nullable=False)
    imagen = database.Column(database.String, nullable=True)
    #tienda_id = database.Column(database.Integer, database.Foreignkey("tienda.id"))
    #categoria_id = database.Column(database.Integer, database.Foreignkey("categoria.id"))
    activo = database.Column(database.Integer, nullable=False)
    stock = database.Column(database.Float, nullable=False)

    def __str__(self):
        return f"<Producto {self.id} {self.nombre} {self.referencia} {self.costo} {self.precio_venta} {self.activo} {self.stock}>"

    def __init__(self, id):
        self.id = id

    def __init__(self, id, nombre, referencia, costo, precio_venta):
        self.id = id
        self.nombre = nombre
        self.referencia = referencia
        self.costo = costo
        self.precio_venta = precio_venta
        self.activo = activo
        self.stock = stock
    
    @staticmethod
    def get_all():
        return Producto.query.all()

    @staticmethod
    def count_records():
        return Producto.query.count()          

    def update(self):
        productoActualiza = Producto.query.filter_by(id=self.id).first()
        productoActualiza.nombre = self.nombre
        productoActualiza.referencia = self.referencia
        productoActualiza.costo = self.costo
        productoActualiza.precio_venta = self.precio_venta
        productoActualiza.stock = self.stock
        database.session.commit()
        return productoActualiza

    def delete(self):
        #print(self.id)
        productoActualiza = Producto.query.filter_by(id=self.id).first()
        #print(productoActualiza)
        productoActualiza.activo = 0
        database.session.commit()
        return 1

    def save(self):
        self.categoria_id = 2
        self.tienda_id = 1
        self.imagen = ""
        print(self)
        database.session.add(self)
        database.session.commit()

    def get_by_id(id):
        return Producto.query.filter_by(id=id).firts       
