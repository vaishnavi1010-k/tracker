from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# In-memory storage
bugs = []

# HTML Templates inside Python
index_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Bug Tracker</title>
</head>
<body>
    <h1>Bug Tracker</h1>
    <a href="/add">Add Bug</a>
    <ul>
        {% for bug in bugs %}
        <li>
            <b>{{ bug.title }}</b><br>
            {{ bug.description }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

add_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Add Bug</title>
</head>
<body>
    <h1>Add Bug</h1>
    <form method="POST">
        <input type="text" name="title" placeholder="Bug Title" required><br><br>
        <textarea name="description" placeholder="Bug Description"></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
    <br>
    <a href="/">Back</a>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(index_page, bugs=bugs)

@app.route('/add', methods=['GET', 'POST'])
def add_bug():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        bugs.append({'title': title, 'description': description})
        return redirect('/')
    return render_template_string(add_page)

# IMPORTANT for Render
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)