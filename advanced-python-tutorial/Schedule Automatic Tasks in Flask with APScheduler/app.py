# pip install flask flask_apscheduler

from flask import Flask, render_template
from flask_apscheduler import APScheduler

from utils import log_ram_usage, log_cpu_usage, print_message

app = Flask(__name__, template_folder="templates")

scheduler = APScheduler()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/other")
def other():
    scheduler.remove_job('messagejob')
    return render_template("other.html")


if __name__ == "__main__":
    scheduler.add_job(func=log_cpu_usage, trigger="interval", seconds=5, id="cpujob")
    scheduler.add_job(func=log_ram_usage, trigger="interval", seconds=10, id="ramjob")
    scheduler.add_job(
        func=print_message,
        args=("My Message",),
        trigger="interval",
        seconds=2,
        id="messagejob",
    )
    scheduler.start()
    app.run(host="0.0.0.0", port=5555, debug=False)
