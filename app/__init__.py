from flask import Flask
from flask_sqlalchemy import SQLAlchemy    # from flask_(nome do modulo) import (classe) 

app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'      # URI de conexao com o banco de dados,ou seja, o caminho que passar até o banco de dados (estabelecer a conexão)
db = SQLAlchemy(app)    # SQLAlchemy(instancia do flask)

from app.controllers import default


 