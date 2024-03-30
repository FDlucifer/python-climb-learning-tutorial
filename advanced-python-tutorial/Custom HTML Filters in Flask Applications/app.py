# pip install flask

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html", some_text="hello world")


@app.template_filter("reverse_string")
def reverse_string_filter(s):
    return s[::-1]

@app.template_filter("alternate")
def alternate_filter(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(s)])

@app.template_filter("repeat")
def repeat_filter(s, times=1):
    return s * times


if __name__ == "__main__":
    app.run(debug=True)
