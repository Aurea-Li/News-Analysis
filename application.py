from flask import Flask, flash, redirect, render_template, request, session


# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        if not request.form.get("query"):
            return render_template("apology.html")

        return render_template("output.html", query = request.form.get("query"))

    else:
        return render_template("index.html")
