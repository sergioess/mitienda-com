
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for


app = Flask(__name__)
app.config.from_object('config')


database = SQLAlchemy(app)


#ACA LAS IMPORTACION DE LAS RUTAS
from routes.categoria_bp import categoria_bp

from routes.usuario_bp import usuario_bp





#ACA REGISTRAMOS LAS RUTAS
app.register_blueprint(categoria_bp, url_prefix='/categoria')

app.register_blueprint(usuario_bp, url_prefix='/usuario')





@app.route("/")
def hello():
    return "Hello Login"


if __name__ == '__main__':
    app.run(debug=True)
