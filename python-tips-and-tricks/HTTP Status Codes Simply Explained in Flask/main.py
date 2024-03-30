from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello", str(10/0)


@app.route("/old_link")
def old_link():
    return redirect(url_for("index"), code=301)


if __name__ == "__main__":
    app.run(debug=True)
