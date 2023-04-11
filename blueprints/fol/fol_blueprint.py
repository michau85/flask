from flask import Blueprint

fol_blueprint = Blueprint('fol_blueprint', __name__)

@fol_blueprint.route('/fol')
def fol():
    return "Fol"
@fol_blueprint.route('/fol2')
def fol2():
    return "Fol2"