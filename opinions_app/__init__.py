import importlib

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings.Config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

importlib.import_module('opinions_app.views')
importlib.import_module('opinions_app.error_handlers')
importlib.import_module('opinions_app.cli_commands')
