from app import app, db
from flask import render_template, request, redirect
import logging
from models import Article

logger = logging.getLogger('app')


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        art = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(art)
            db.session.commit()
            return redirect('/home')
        except Exception as ex:
            logger.warning(ex)
            return 'Error'
    else:
        return render_template('create.html')


@app.route('/contacts')
def contacts():
    return "It's my contacts"


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + '-' + str(id)
