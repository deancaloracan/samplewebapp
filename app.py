from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # Initialize Flask

# Initialize task ID counter
task_id_counter = 2

# Placeholder for tasks with unique IDs
todos = [{"id": 0, "task_description": "Buy groceries", "done": False},
         {"id": 1, "task_description": "Read a book", "done": False},
         {"id": 2, "task_description": "Study Flask", "done": False}]

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_id_counter
    if request.method == 'POST':
        task_content = request.form['new_todo']
        if task_content:
            task_id_counter += 1  # Increment ID for each new task
            todos.append({"id": task_id_counter, "task_description": task_content, "done": False})
        return redirect(url_for('index'))
    return render_template('index.html', todos=todos)

@app.route('/toggle_status/<int:todo_id>')
def toggle_status(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            break
    return redirect(url_for('index'))

@app.route('/remove/<int:todo_id>')
def remove_task(todo_id):
    global todos # Variable na list
    todos = [todo for todo in todos if todo['id'] != todo_id] # If you niloop mong todos ay hindi same ng id which we want to delete
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_task(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if request.method == 'POST':
        task_description = request.form['edited_todo']
        if todo and task_description:
            todo['task_description'] = task_description
        return redirect(url_for('index'))
    return render_template('edit_task.html', todo=todo)
        

if __name__ == '__main__': # Define port, host, and debugging while running
    app.run(debug=True)