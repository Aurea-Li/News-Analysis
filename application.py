from flask import Flask, flash, redirect, render_template, request, session, send_file
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy
import matplotlib.pyplot as plt
from helper import addEvent

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

        query = request.form.get("query")

        return render_template("output.html", query = query)

    else:
        return render_template("index.html")


# Embed graph
@app.route("/fig/<query>")
def fig(query):

    # Obtain dict from query
    delaydict = addEvent(query)


    # Create matplotlib figure
    fig, ax = plt.subplots(1)
    plt.bar(range(len(delaydict)), [delaydict[key][2] for key in delaydict], align='center')
    plt.xticks(range(len(delaydict)), [key for key in delaydict])

    # Add labels, configure graph
    plt.xticks(rotation=45)
    plt.ylabel('Minutes')
    plt.title('Average Publish Delay')
    plt.tight_layout()


    # Converting it to bytes
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)

    return send_file(img, mimetype='/png')
