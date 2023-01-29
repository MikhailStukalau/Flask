from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/contacts')
def contacts():
    return "It's my contacts"


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + '-' + str(id)