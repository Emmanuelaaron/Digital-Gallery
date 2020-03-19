from flask import Flask

def create_app(test_config=None):
  app = Flask(__name__)

  @app.route('/')
  def index():
    return "Hello Digital Chena"
  return app
