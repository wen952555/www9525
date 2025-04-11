import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# 加载配置
app.config.from_object('config.Config')

# 提供 favicon.ico 支持，避免 404 错误
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# 用户认证相关路由
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

# 流量统计相关路由
@app.route('/traffic/stats', methods=['GET'])
def traffic_stats():
    # 示例流量数据
    stats = {
        "total_traffic": "120GB",
        "used_traffic": "50GB",
        "remaining_traffic": "70GB"
    }
    return jsonify(stats)

# 管理面板相关路由
@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    # 示例管理数据
    data = {
        "active_users": 120,
        "online_users": 45,
        "server_load": "30%"
    }
    return jsonify(data)

# 主函数入口
if __name__ == "__main__":
    # Render 平台会自动设置 PORT 环境变量
    port = os.environ.get("PORT")
    if port is None or not port.isdigit():
        port = 5000  # 默认端口
    app.run(host="0.0.0.0", port=int(port))