from flask import Flask, request, render_template
from database_functions import send_to_database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "POST": send_to_database(request.form["name"], request.form["phone"])
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
