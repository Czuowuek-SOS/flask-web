from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

from users import User, db

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.config['SERVER_NAME'] = "parufex.net:6090"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route("/", methods=["GET"])
def home():
    print("visitor: ", jsonify({'ip': request.remote_addr}))
    return render_template("index.html")

@app.route("/films")
def films():
    return render_template("films.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("/log.html")

@app.route("/myip", methods=["GET"])
def myip():
    return jsonify({'ip': request.remote_addr}), 200

if  __name__ == "__main__":
    app.run(debug=True)
