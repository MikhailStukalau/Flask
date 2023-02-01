import logging
from logging.config import dictConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import LOGGING
import os

basedir = os.path.abspath(os.path.dirname(__file__))
dictConfig(LOGGING)

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.logger = logging.getLogger('app')

db = SQLAlchemy(app)

import views
db.create_all()


