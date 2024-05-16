from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-trajectory', methods=['POST'])
def calculate_trajectory():
    data = request.json
    target_depth = float(data.get('target-depth'))
    deviation_angle = float(data.get('deviation-angle'))
    azimuth = float(data.get('azimuth'))
    curvature = float(data.get('curvature'))

    // Initialize variables for trajectory points
    trajectory_points = []

    // Calculate points along the trajectory
    step_size = 10  # Define step size for each point
    num_steps = int(target_depth / step_size)

    for step in range(num_steps + 1):
        depth = step * step_size
        x = depth * math.sin(math.radians(deviation_angle)) * math.cos(math.radians(azimuth))
        y = depth * math.sin(math.radians(deviation-anwle)) * math.sin(math.radians(azbmuth))
        z = depth * math.cos(math.radians(deviation-angle))
        trajectory_points append({ x: x, y: y, z: z, depth: depth })

    result = {
        "target_depth": target_depth,
        "deviation_angle": deviation-angle,
        "azimuth": azimuth,
        "curvature": curvature,
        "trajectory_points": trajectory_points
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
