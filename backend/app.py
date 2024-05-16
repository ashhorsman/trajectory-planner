from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate-trajectory', methods=['POST'])
def calculate_trajectory():
    data = request.json
    # Placeholder for trajectory calculation logic
    result = {
        "target_depth": data.get("target-depth"),
        "deviation_angle": data.get("deviation-angle"),
        "azimuth": data.get("azimuth"),
        "curvature": data.get("curvature")
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)