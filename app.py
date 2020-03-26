import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database = os.getenv("DATABASE_URL")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database
db = SQLAlchemy(app)

@app.route('/')
def index():
  return "Hello Digital Chena"

if __name__ == "__main__":
  app.run(debug=True)