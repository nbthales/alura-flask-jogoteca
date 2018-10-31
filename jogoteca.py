from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)  # aplicação sendo criada
app.config.from_pyfile('config.py')  # configuração da aplicação

db = MySQL(app)  # configuração do bd

from views import *

if __name__ == '__main__':
    app.run(debug=True)
