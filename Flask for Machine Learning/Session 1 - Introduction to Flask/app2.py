from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # return "<h2> Welcome bro </h2>"
    return render_template("./index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    data = {'name': None}
    if request.method == "POST":
        name = request.form.get("name")
        data = {'name': name}
    return render_template("about.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)