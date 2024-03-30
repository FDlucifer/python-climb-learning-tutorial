# pip install flask

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world!"


if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))
