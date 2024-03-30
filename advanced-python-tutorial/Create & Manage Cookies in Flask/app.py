# pip install flask

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/new_cookie")
def new_cookie():
    response = make_response("hello world!")
    response.set_cookie("mycookie", "myvalue")
    return response

@app.route("/show_cookie")
def show_cookie():
    cookie_value = request.cookies.get("mycookie")
    return cookie_value

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=9999)
