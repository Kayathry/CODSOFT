from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    complete = db.Column(db.Boolean)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    description = request.form.get("description")
    new_todo = Todo(title=title, description=description, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/change_complete_status/<int:todo_id>")
def change_complete_status(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.id = todo_id
    todo.title = request.form.get("title")
    todo.description = request.form.get("description")
    todo.complete = todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:todo_id>")
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    return render_template('edit.html', todo=todo)


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)



