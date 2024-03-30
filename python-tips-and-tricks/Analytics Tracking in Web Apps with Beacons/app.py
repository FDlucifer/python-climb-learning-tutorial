# pip install flask pandas

import os
import pandas as pd

from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/a")
def endpoint_a():
    return render_template("endpoint_a.html")


@app.route("/b")
def endpoint_b():
    return render_template("endpoint_b.html")


@app.route("/track_time", methods=["POST"])
def track_time():
    endpoint = request.json["endpoint"]
    time_spent = request.json["time"]

    if os.path.exists("tracker.csv"):
        df = pd.read_csv("tracker.csv", index_col="endpoint")
        if endpoint in df.index.values:
            df.at[endpoint, "time"] += float(time_spent)
        else:
            df.loc[endpoint] = float(time_spent)
    else:
        df = pd.DataFrame(columns=["time"])
        df.loc[endpoint] = time_spent

    df.to_csv("tracker.csv", index=True, index_label="endpoint")

    return ""


if __name__ == "__main__":
    app.run(debug=True)
