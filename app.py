
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Dev, Prod


app = Flask(__name__, static_folder='uploads')
# Allow CORS for all routes
CORS(app)
app.config.from_object(Dev)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
