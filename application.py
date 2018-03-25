from flask import Flask, flash, redirect, render_template, request, session

from helper.py import AddEvent

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

    from io import BytesIO


    if request.method == "POST":

        if not request.form.get("query"):
            return render_template("apology.html")

        q = request.form.get("query")


        response.headers['Content-Type'] = 'image/png'

        return render_template("output.html")

    else:
        return render_template("index.html")


# TODO: Embed python graph 

@app.route("/fig")
def fig():
    # Obtain graph from query
    fig = AddEvent(q)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
