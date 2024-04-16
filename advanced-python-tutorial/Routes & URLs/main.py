from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>hello world</h1>"


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "you made a GET request\n"
    elif request.method == "POST":
        return "you made a POST request\n"
    else:
        return "you will never see this message\n"


@app.route("/greet/<name>")
def greet(name):
    return f"hello {name}"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route("/handle_url_params")
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args["greeting"]
        name = request.args.get("name")
        return f"{greeting}, {name}"
    else:
        return "some parameters are missing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
