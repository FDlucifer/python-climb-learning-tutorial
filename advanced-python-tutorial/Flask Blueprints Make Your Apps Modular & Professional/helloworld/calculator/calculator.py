from flask import Blueprint, render_template, redirect, url_for

calculator_bp = Blueprint("calculator", __name__)

@calculator_bp.route("/")
def index():
    return "this is the calculator blueprint!"

@calculator_bp.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return str(num1 + num2)

@calculator_bp.route("/subtract/<int:num1>/<int:num2>")
def subtract(num1, num2):
    return str(num1 - num2)

@calculator_bp.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
    return str(num1 * num2)

@calculator_bp.route("/divide/<int:num1>/<int:num2>")
def divide(num1, num2):
    return str(num1 / num2)

@calculator_bp.route("/go_to_hello")
def go_to_hello():
    return redirect(url_for("helloworld.hello_html"))
