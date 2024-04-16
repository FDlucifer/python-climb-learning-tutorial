# pip install Flask requests
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    url = request.form.get("url")

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    try:
        response = requests.get(url, timeout=10)
        if response.status_code < 400:
            status = "UP"
        else:
            status = "DOWN"
    except requests.RequestException:
        status = "DOWN"

    return render_template("results.html", url=url, status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
