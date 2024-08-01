from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def read_todos():
    with open('todo.txt', 'r') as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]

def write_todos(todos):
    with open('todo.txt', 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form['new_todo']
        todos = read_todos()
        todos.append(new_todo)
        write_todos(todos)
        return redirect(url_for('index'))
    else:
        todos = read_todos()
        return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)
