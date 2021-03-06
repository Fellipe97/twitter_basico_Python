from flask import Flask
from flask_sqlalchemy import SQLAlchemy    # from flask_(nome do modulo) import (classe) 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config') 

db = SQLAlchemy(app)    # SQLAlchemy(instancia do flask)
migrate = Migrate (app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default

