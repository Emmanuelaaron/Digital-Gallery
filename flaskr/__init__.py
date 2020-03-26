import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database = os.getenv("db_url")

def create_app(test_config=None):
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = database
  db = SQLAlchemy(app)

  @app.route('/')
  def index():
    return "Hello Digital Chena"
  return app
