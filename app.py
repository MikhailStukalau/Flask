import logging
from logging.config import dictConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import LOGGING


dictConfig(LOGGING)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.logger = logging.getLogger('app')
app.logger.info("App started")
db = SQLAlchemy(app)

import views
