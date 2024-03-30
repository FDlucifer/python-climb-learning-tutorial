from flask import Blueprint, render_template, redirect

helloworld_bp = Blueprint("helloworld", __name__, template_folder="templates")

@helloworld_bp.route("/")
def index():
    return "hello world!"

@helloworld_bp.route("/hello")
def hello():
    return "hello world again!"

@helloworld_bp.route("/hello/<name>")
def hello_name(name):
    return f"hello {name}!"

@helloworld_bp.route("/hellohtml")
def hello_html():
    return render_template("helloworld/hello.html")
