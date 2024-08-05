from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize task ID counter
task_id_counter = 3

# Placeholder for tasks with unique IDs
tasks = [{"id": 1, "content": "Buy groceries", "done": False},
         {"id": 2, "content": "Read a book", "done": False},
         {"id": 3, "content": "Study Flask", "done": False}]

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_id_counter
    if request.method == 'POST':
        task_content = request.form['new_todo']
        if task_content:
            task_id_counter += 1  # Increment ID for each new task
            tasks.append({"id": task_id_counter, "content": task_content, "done": False})
        return redirect(url_for('index'))
    return render_template('index.html', todos=tasks)

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/toggle_status/<int:task_id>')
def toggle_status(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)