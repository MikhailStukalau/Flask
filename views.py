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


@app.route('/post')
def post():
    articles = Article.query.order_by(Article.date).all()
    return render_template('posts.html', articles=articles)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        art = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(art)
            app.logger.info(f"Entry with title {title} added!")
            db.session.commit()
            return redirect('/home')
        except Exception as ex:
            logger.warning(ex)
            return 'Error'
    else:
        return render_template('create.html')


@app.route('/<int:id>/details/', methods=['GET'])
def details(id):
    detail = None
    try:
        detail = Article.query.get_or_404(id)
        db.session.commit()
        if detail is None:
            flash('Нет записи с таким идентификатором', 'danger')
            abort(404)
    except SQLAlchemyError as ex:
        log_error('Error while querying database', exc_info=ex)
        flash('Во время запроса произошла непредвиденная ошибка', 'danger')
        abort(500)
    return render_template('details.html', detail=detail)


@app.route('/contacts')
def contacts():
    return "It's my contacts"


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + '-' + str(id)
