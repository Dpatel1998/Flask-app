from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@34.105.177.69:3306/todo_app'

db = SQLAlchemy(app)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default=False)

@app.route("/")
def index():
    all_todos = Todos.query.all()
    todos_string = ""
    for todo in all_todos:
        todos_string += "<br>" + str(todo.id) + todo.task + " " + str(todo.complete)
    return todos_string

@app.route("/add")
def add():
    new_todo = Todos(task="New Todo")
    db.session.add(new_todo)
    db.session.commit()
    return new_todo.task 

@app.route("/complete/<int:todo_id>") 
def complete(todo_id):
    todo = Todos.query.get(todo_id) 
    todo.complete = True
    db.session.commit()
    return "Completed Todo"

@app.route("/incomplete/<int:todo_id>") 
def incomplete(todo_id):
    todo = Todos.query.get(todo_id) 
    todo.complete = False
    db.session.commit()
    return "Incompleted Todo"

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todos.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
