from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
# from flask_login import LoginManager

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nodes.sqlite3'  
app.config['SECRET_KEY'] = "secret key"  
  
db = SQLAlchemy(app)  
from app import routes