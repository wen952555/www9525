from flask import Flask, request, jsonify
from admin.admin import AdminManager
from user.auth import login
from user.restriction import is_user_restricted, restrict_user, unrestrict_user

app = Flask(__name__)

# Initialize admin manager
admin_manager = AdminManager()

@app.route("/")
def home():
    return "Welcome to the VPN Service Bot!"

@app.route("/user/login", methods=["POST"])
def user_login():
    user_id = request.json.get("user_id")
    if is_user_restricted(user_id):
        return jsonify({"error": "You are restricted from accessing this bot."}), 403
    return login(user_id)

@app.route("/admin/restrict", methods=["POST"])
def admin_restrict_user():
    admin_id = request.json.get("admin_id")
    user_id = request.json.get("user_id")
    if not admin_manager.is_admin(admin_id):
        return jsonify({"error": "Unauthorized access."}), 403
    restrict_user(user_id)
    return jsonify({"message": f"User {user_id} has been restricted."})

@app.route("/admin/unrestrict", methods=["POST"])
def admin_unrestrict_user():
    admin_id = request.json.get("admin_id")
    user_id = request.json.get("user_id")
    if not admin_manager.is_admin(admin_id):
        return jsonify({"error": "Unauthorized access."}), 403
    unrestrict_user(user_id)
    return jsonify({"message": f"User {user_id} has been unrestricted."})

@app.route("/admin/list_restricted", methods=["GET"])
def admin_list_restricted_users():
    admin_id = request.args.get("admin_id")
    if not admin_manager.is_admin(admin_id):
        return jsonify({"error": "Unauthorized access."}), 403
    return jsonify({"restricted_users": admin_manager.list_restricted_users()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)