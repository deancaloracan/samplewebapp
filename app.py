from flask import Flask, render_template

app = Flask(__name__)

# Sample data to display in the UI
def get_sample_todos():
    return ["Buy groceries", "Read a book", "Study Flask"]

@app.route('/', methods=('GET', 'POST'))
def index():
    todos = get_sample_todos()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)
