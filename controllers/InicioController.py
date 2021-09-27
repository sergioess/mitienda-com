from flask import Flask

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.categoria import Categoria
from models.producto import Producto


# app = Flask(__name__)
# app.config.from_object('config')

def home():
    categoriasTotal = Categoria.count_records()
    productosTotal = Producto.count_records()
    return render_template('/home.html', totalcategoria=categoriasTotal, totalproducto=productosTotal)

def index():
    return render_template('/index.html')