import pandas as pd
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    send_from_directory,
    redirect,
)

app = Flask(__name__, template_folder="templates")
todos = []


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    todos.append(todo)
    return redirect(url_for("index"))

@app.route("/remove/<int:index>")
def remove():
    del todos[index-1]
    return redirect(url_for("index"))

@app.route("/download_todos")
def download():
    df = pd.DataFrame({
        'todo_id': list(range(len(todos))),
        'todo': todos
    })

    df.to_excel('todos.xlsx')
    return send_from_directory('.', 'todos.xlsx')

if __name__ == '__main__':
    app.run(debug=True)
