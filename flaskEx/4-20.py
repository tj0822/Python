from flask import Flask
from flask import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql+pypostgresql://sqlalchemy:sqlalchemy@localhost/sqlalchemy"
db = SQLAlchemy(app)

… 중략