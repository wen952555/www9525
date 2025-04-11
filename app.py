import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "VPN Service is running!"

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # 简单的用户验证逻辑
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful", "token": "example_token"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@app.route('/traffic/stats', methods=['GET'])
def traffic_stats():
    stats = {
        "total_traffic": "120GB",
        "used_traffic": "50GB",
        "remaining_traffic": "70GB"
    }
    return jsonify(stats)

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    data = {
        "active_users": 120,
        "online_users": 45,
        "server_load": "30%"
    }
    return jsonify(data)

if __name__ == "__main__":
    # Render 平台会自动设置 PORT 环境变量
    port = os.getenv("PORT", "5000")  # 提供默认值 5000
    try:
        port = int(port)
    except ValueError:
        raise ValueError(f"Invalid port number: {port}. Ensure that the PORT environment variable is set correctly.")
    app.run(host="0.0.0.0", port=port)