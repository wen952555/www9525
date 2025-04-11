from flask import Flask, render_template
from models import User

app = Flask(__name__)

@app.route('/')
def dashboard():
    users = User.query.all()
    return render_template("dashboard.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)