import os
from flask import Flask, jsonify, request

# 创建 Flask 应用
app = Flask(__name__)
app.config.from_object('config.Config')  # 加载配置

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

    # 简单用户校验逻辑
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful", "token": "example_token"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

# 流量统计相关路由
@app.route('/traffic/stats', methods=['GET'])
def get_stats():
    # 示例流量数据
    stats = {
        "total_traffic": "120GB",
        "used_traffic": "50GB",
        "remaining_traffic": "70GB"
    }
    return jsonify(stats)

# 管理面板相关路由
@app.route('/admin/dashboard', methods=['GET'])
def dashboard():
    # 示例管理数据
    data = {
        "active_users": 120,
        "online_users": 45,
        "server_load": "30%"
    }
    return jsonify(data)

# 主函数入口
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render 使用的端口
    app.run(host="0.0.0.0", port=port)