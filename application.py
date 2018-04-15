from flask import Flask, flash, redirect, render_template, request, session, send_file
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
from helper import addEvent, swapArticles

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST", "PUT"])
def index():

    if request.method == "POST":

        if not request.form.get("query"):
            return render_template("apology.html")

        query = request.form.get("query")
        delaydict = addEvent(query)

        return render_template("output.html", query = query, delaydict = delaydict)

    else:
        return render_template("index.html")

@app.route("/update/<delaydict>/<query>/<source>/<i>")
def update(delaydict, query, source, i):


    print(type(delaydict))

    # print(delaydict[str(source)])


    delaydict = swapArticles(delaydict, source, i)
    return render_template("output.html", query = query, delaydict = delaydict)


# Embed graph
@app.route("/fig/<query>")
def fig(query):

    delaydict = addEvent(query)

    # Creating x and y axis
    x = [delaydict[key][0]['delay time'] for key in delaydict]
    y = [delaydict[key][0]['word count'] for key in delaydict]
    labels = [key for key in delaydict]

    # Create matplotlib figure
    fig, ax = plt.subplots(1)
    
    plt.scatter(x, y, color = 'k', s = 25, marker = 'o')
    
    # Adding labels
    #TODO: Labels are sometimes being cut off
    for i, label in enumerate(labels):
        plt.annotate(label, (x[i], y[i]), size = 6)

    plt.xlabel('Delay Time (minutes)')
    plt.ylabel('Word Count')
    plt.title('Average Publish Delay')
    plt.tight_layout()


    # Converting it to bytes
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)

    return send_file(img, mimetype='/png')
