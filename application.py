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


# TODO: Embed python graph 

@app.route("/fig/<query>")
def fig(query):

    # Obtain dict from query
    delaydict = addEvent(query)

    # print(delaydict)

    # Create matplotlib figure
    fig, ax = plt.subplots(1)
    
    plt.bar(range(len(delaydict)), list(delaydict.values()), align='center')
    plt.xticks(range(len(delaydict)), list(delaydict.keys()))
    plt.xticks(rotation=45)
    plt.ylabel('Minutes')
    plt.title('Average Publish Delay')


    # Dummy plot
    # t = numpy.arange(0.0, 2.0, 0.01)
    # s = 1 + numpy.sin(2*numpy.pi*t)
    # fig, ax = plt.subplots(1)
    # plt.plot(t, s)

    # Converting it to bytes
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)

    return send_file(img, mimetype='/png')
