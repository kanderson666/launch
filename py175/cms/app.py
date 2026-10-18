from flask import Flask, render_template, send_from_directory, redirect, flash, url_for, request
import os
from markdown import markdown
from cms.util import valid_filename

app = Flask(__name__)
app.secret_key='secret1'

def get_file_path():
    if app.config['TESTING']:
        args = ('tests', 'data')
    else:
        args = ('cms', 'data')
    
    root = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(root, *args)

    return file_path

def get_contents(filename):
    path = get_file_path()

    with open(f"{path}/{filename}", 'r') as file:
        contents = file.read()
    return contents

@app.route("/")
def index():
    file_path = get_file_path()
    files = os.listdir(file_path)
    
    return render_template('index.html', files=files)

@app.route("/<filename>")
def open_file(filename):
    file_path = get_file_path()
    files = os.listdir(file_path)

    if filename not in files:
        flash(f"{filename} does not exist.")
        return redirect( url_for("index")) 

    if filename.endswith("md"):
        with open(f"{os.path.join(file_path, filename)}", 'r') as markdown_page:
            content = markdown_page.read()
            return render_template('markdown.html', content=markdown(content))

    return send_from_directory(file_path, filename)

@app.route("/<filename>/edit")
def edit_file(filename):
    contents = get_contents(filename)
    return render_template('edit.html', filename=filename, contents=contents)

@app.route("/<filename>/edit", methods=['POST'])
def update_contents(filename):
    contents = request.form['file_contents']
    file_path = get_file_path()

    with open(f"{os.path.join(file_path, filename)}", 'w') as file:
        file.write(contents)

    flash(f'{filename} has been updated.')
    return redirect(url_for('index'))

@app.route("/create_doc")
def new_doc():
    return render_template('create_doc.html')

@app.route("/create_doc", methods=['POST'])
def create_doc():
    filename = request.form['filename']

    if not valid_filename(filename):
        flash("A name and valid extension are required")
        return render_template('create_doc.html'), 422
    
    file_path = get_file_path()
    with open(os.path.join(file_path, filename), 'w') as file:
        file.write('')

    flash(f"{filename} has been created.")
    return redirect(url_for("index"))

@app.route("/<filename>/delete", methods=['POST'])
def delete(filename):
    file_path = get_file_path()
    files = os.listdir(file_path)

    if filename not in files:
        flash(f"{filename} does not exist.")
        return render_template("index.html"), 422
    
    os.remove(os.path.join(file_path, filename))
    flash(f"{filename} has been deleted.")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5003)
