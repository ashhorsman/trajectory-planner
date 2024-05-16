from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trajectory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_depth = db.Column(db.Float, nullable=False)
    deviation_angle = db.Column(db.Float, nullable=False)
    azimuth = db.Column(db.Float, nullable=False)
    curvature = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Trajectory {self.id}>'
