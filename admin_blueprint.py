from flask import Blueprint

admin_blueprint = Blueprint('admin_blueprint', __name__)

@admin_blueprint.route('/ad')
def index():
    return "This is admin"
