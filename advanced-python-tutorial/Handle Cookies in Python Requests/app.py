# pip install flask requests

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == "testuser" and password == "testpass":
        res = make_response(jsonify(success=True))
        res.set_cookie("session", "logged_in")
        return res
    else:
        return jsonify(success=False), 401


@app.route("/protected")
def protected():
    session_cookie = request.cookies.get("session")
    if session_cookie == "logged_in":
        return jsonify(access=True)
    else:
        return jsonify(access=False), 403


if __name__ == "__main__":
    app.run(debug=True)
