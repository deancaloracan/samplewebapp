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

if __name__ == '__main__': # Define port, host, and debugging while running
    app.run(debug=True)