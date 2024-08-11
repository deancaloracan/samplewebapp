from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__) # Initialize Flask

# Configuring the PostgreSQL database with the URL from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables modification tracking for performance

db = SQLAlchemy(app)  # Sets up SQLAlchemy with the Flask app for database interactions

# # Initialize task ID counter
# task_id_counter = 2

# # Placeholder for tasks with unique IDs
# todos = [{"id": 0, "task_description": "Buy groceries", "done": False},
#          {"id": 1, "task_description": "Read a book", "done": False},
#          {"id": 2, "task_description": "Study Flask", "done": False}]

# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global task_id_counter
#     if request.method == 'POST':
#         task_content = request.form['new_todo']
#         if task_content:
#             task_id_counter += 1  # Increment ID for each new task
#             todos.append({"id": task_id_counter, "task_description": task_content, "done": False})
#         return redirect(url_for('index'))
#     return render_template('index.html', todos=todos)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['new_todo']
        if task_content:
            new_task = Todo(task_description=task_content, done=False)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

# @app.route('/toggle_status/<int:todo_id>')
# def toggle_status(todo_id):
#     for todo in todos:
#         if todo['id'] == todo_id:
#             todo['done'] = not todo['done']
#             break
#     return redirect(url_for('index'))

@app.route('/toggle_status/<int:todo_id>')
def toggle_status(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        todo.done = not todo.done
        db.session.commit()
    return redirect(url_for('index'))

# @app.route('/remove/<int:todo_id>')
# def remove_task(todo_id):
#     global todos # Variable na list
#     todos = [todo for todo in todos if todo['id'] != todo_id] # If you niloop mong todos ay hindi same ng id which we want to delete
#     return redirect(url_for('index'))

@app.route('/remove/<int:todo_id>')
def remove_task(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('index'))

# @app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
# def edit_task(todo_id):
#     todo = next((todo for todo in todos if todo['id'] == todo_id), None)
#     if request.method == 'POST':
#         task_description = request.form['edited_todo']
#         if todo and task_description:
#             todo['task_description'] = task_description
#         return redirect(url_for('index'))
#     return render_template('edit_task.html', todo=todo)

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_task(todo_id):
    todo = Todo.query.get(todo_id)
    if request.method == 'POST':
        task_description = request.form['edited_todo']
        if todo and task_description:
            todo.task_description = task_description
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_task.html', todo=todo)
        

if __name__ == '__main__': # Define port, host, and debugging while running
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)