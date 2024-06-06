from flask import Flask, render_template, request, redirect
import streamlit as st

app = Flask(__name__)

@app.route("/")
def home():
    # return "<h2> Welcome bro </h2>"
    return render_template("./index.html")

@app.route("/about/<name>")
def about(name):
    data = {'name': name}
    if request.method == "POST":
        name = request.form.get("name")
        data = {'name': name}
    else :
        name = "Mate"
    return render_template("about.html", data=data)

@app.route("/dashboard")
def dashoard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)