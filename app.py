from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for

app = Flask(__name__)
app.config.from_object('config')
from flask import send_from_directory

database = SQLAlchemy(app)

#ACA LAS IMPORTACION DE LAS RUTAS
from routes.categoria_bp import categoria_bp
from routes.producto_bp import producto_bp
from routes.usuario_bp import usuario_bp
from routes.entrada_bp import entrada_bp
from routes.salida_bp import salida_bp
from routes.inicio_bp import inicio_bp


#ACA REGISTRAMOS LAS RUTAS
app.register_blueprint(categoria_bp, url_prefix='/categoria')
app.register_blueprint(producto_bp, url_prefix='/producto')
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(entrada_bp, url_prefix='/entrada')
app.register_blueprint(salida_bp, url_prefix='/salida')


app.register_blueprint(inicio_bp, url_prefix='/')
# @app.route("/")
# def hello():

#     return render_template('/index.html')

@app.route('/img/<nombreFoto>')
def uplproductos(nombreFoto):
    return send_from_directory(app.config['CARPETA_IMG'], nombreFoto)

@app.route("/login")
def hello2():
    return "Hello Login"    


if __name__ == '__main__':
    app.run(debug=True)
