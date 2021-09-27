from flask import Blueprint

from controllers.TiendaController import index, store, show, update, destroy, create

tienda_bp = Blueprint(
    'tienda_bp', __name__, template_folder='templates/tienda')
tienda_bp.route('/', methods=['GET'])(index)
tienda_bp.route('/create', methods=['GET'])(create)
tienda_bp.route('/store', methods=['POST'])(store)
tienda_bp.route('/<int:tienda_id>', methods=['GET'])(show)
tienda_bp.route('/update', methods=['POST'])(update)
tienda_bp.route('/destroy/<int:tienda_id>',methods=['GET', 'POST', 'DELETE'])(destroy)