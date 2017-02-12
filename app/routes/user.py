from flask import Blueprint
from flask_jwt import jwt_required, current_identity

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/')
@jwt_required()
def me():
    return '%s' % current_identity
