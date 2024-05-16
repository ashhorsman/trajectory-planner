from flask import Blueprint, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})