from flask import Blueprint

from controllers.UsuarioController import index, store, show, update, destroy, create

usuario_bp = Blueprint(
    'usuario_bp', __name__, template_folder='templates/usuario')
usuario_bp.route('/', methods=['GET'])(index)
usuario_bp.route('/create', methods=['GET'])(create)
usuario_bp.route('/store', methods=['POST'])(store)
usuario_bp.route('/<int:clasificacion_id>', methods=['GET'])(show)
usuario_bp.route('/update/<int:clasificacion_id>', methods=['PUT'])(update)
usuario_bp.route('/destroy/<int:clasificacion_id>',
                   methods=['GET', 'POST', 'DELETE'])(destroy)