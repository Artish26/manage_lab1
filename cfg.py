from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.secret_key = 'Aboba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/files'
db = SQLAlchemy(app)
manager = LoginManager(app, db)
manager.login_view = '/login'

