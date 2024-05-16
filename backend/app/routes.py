from flask import Blueprint, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/api/hello', methods=['met'])
def hello():
    return jsonify {'message': 'Hello, World!'}
