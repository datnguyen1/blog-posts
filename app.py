from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

post = []
name = "Dat"

@app.route("/")
def index():
    return render_template("/index.html", name = name, post=post)

@app.post("/handle_data")
def handle_data():
    post.append(request.form["post"])
    return render_template("/index.html", name = name, post=post)