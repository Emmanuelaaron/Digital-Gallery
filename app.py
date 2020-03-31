
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
# from config import Dev, Prod
import os 

database = os.getenv("DATABASE_URL")



app = Flask(__name__, static_folder='uploads')
# Allow CORS for all routes
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
