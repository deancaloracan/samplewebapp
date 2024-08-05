from flask import Flask, render_template

app = Flask(__name__) # Initialize Flask

# dummy data
def get_sample_todos():
    return ["Buy groceries", "Read a book", "Study Flask", "DEADAENAODNOAEDNOANDOIANDOIASNDOIANDOIA"]

@app.route('/', methods=('GET', 'POST')) # Define route
def index():  # Define what it would present or do
    todos = get_sample_todos()
    return render_template('index.html', todos=todos) # Defining html to render

if __name__ == '__main__': # Define port, host, and debugging while running
    app.run(debug=True)