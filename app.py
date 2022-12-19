from flask import Flask, render_template, request, redirect, url_for, jsonify
from fileinput import filename

from flask_sqlalchemy import SQLAlchemy

# from users import User, db


UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
# app.config['SERVER_NAME'] = "localhost:6090"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config["SLQALCHEMY_DATABASE_URI"] = "sqlite:///accounts.sqlite3"

db = SQLAlchemy(app)

class Accounts(db.Model):
    id = db.Column('account_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))  
    pasword = db.Column(db.String(200))
    ip = db.Column(db.String(10))

    def __init__(self, name, email, password, ip):
        self.name = name
        self.email = email
        self.pasword = password
        self.ip = ip
db.create_all()


@app.route("/", methods=["GET"])
def home():
    print("visitor: ", jsonify({'ip': request.remote_addr}))
    return render_template("index.html")

@app.route("/films")
def films():
    return render_template("films.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signin", methods=["POST", "GET"])
def login():

    if request.method == "POST":   
        print("post")
        
    return render_template("/log.html")

@app.route("/myaacount")
def myaccount():
    return 'sesx'

@app.route("/myip", methods=["GET"])
def myip():
    return jsonify({'ip': request.remote_addr}), 200

if  __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
