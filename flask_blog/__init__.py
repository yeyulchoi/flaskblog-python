from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] ='c8c88516d9a0952381d92fc0cc0ffb74'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from flask_blog import routes