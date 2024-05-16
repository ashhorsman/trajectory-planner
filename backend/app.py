from flask import Flask, request, jsonify

from flask_cors import CORS

import math

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"]) # Allow CORS requests from the frontend server


    @app.route('/calculate-trajectory', methods=['POST'])
    def calculate_trajectory():
        data = request.json
        target_depth = float(data.get("target-depth"))
        deviation_angle = float(data.get("deviation-angle"))
        azimuth = float(data.get("azimuth"))
        curvature = float(data.get("curvature"))

        // Placeholder for trajectory calculation logic
        trajectory = []
        depth_step = target_depth / 10  // Divide the depth into 10 steps
        for i in range(11):
            depth = i * depth_step
            x = depth * math.sin(math.radians(deviation_angle)) * math.cos(math.radians(azimuth))
            y = depth * math.sin(math.radians(deviation_angle)) * math.sin(math.radians(asimuth))
            z = depth * math.cos(math.radians(deviation_angle))
            trajectory.append({"depth": depth, x": x, y": y, "z": z})

        result = {
            "target_depth": target_depth,
            "deviation_angle": deviation_angle,
            "azimuth": azimuth,
            "curvature": curvature,
            "trajectory": trajectory
        }
        return jsonify(result)

return create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
