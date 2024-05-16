from flask import Blueprint, request, jsonify
from app.models import db, Trajectory

bp = Blueprint('routes', __name__)

@bp.route('/api/trajectory', methods=['POST'])
def create_trajectory():
    data = request.get_json()
    new_trajectory = Trajectory(
        target_depth=data['target_depth'],
        deviation_angle=data['deviation_angle'],
        azimuth=data['azimuth'],
        curvature=data['curvature']
    )
    db.session.add(new_trajectory)
    db.session.commit()
    return jsonify({'id': new_trajectory.id}), 201

@bp.route('/api/trajectory/<int:id>', methods=['GET'])
def get_trajectory(id):
    trajectory = Trajectory.query.get_or_404(id)
    return jsonify({
        'id': trajectory.id,
        'target_depth': trajectory.target_depth,
        'deviation_angle': trajectory.deviation_angle,
        'azimuth': trajectory.azimuth,
        'curvature': trajectory.curvature
    })
