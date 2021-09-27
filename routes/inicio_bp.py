from flask import Blueprint

from controllers.InicioController import index

inicio_bp = Blueprint('inicio_bp', __name__, template_folder='templates/')
inicio_bp.route('/', methods=['GET'])(index)
# TODO
inicio_bp.route('/login', methods=['GET'])(index)
inicio_bp.route('/logout', methods=['GET'])(index)
