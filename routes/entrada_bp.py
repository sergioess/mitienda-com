from flask import Blueprint

from controllers.EntradaController import index, store, show, update, destroy, create

entrada_bp = Blueprint(
    'entrada_bp', __name__, template_folder='templates/entrada')
entrada_bp.route('/', methods=['GET'])(index)
entrada_bp.route('/create', methods=['GET'])(create)
entrada_bp.route('/store', methods=['POST'])(store)
entrada_bp.route('/<int:entrada_id>', methods=['GET'])(show)
entrada_bp.route('/update/<int:entrada_id>', methods=['PUT'])(update)
entrada_bp.route('/destroy/<int:entrada_id>',
                   methods=['GET', 'POST', 'DELETE'])(destroy)