from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


from routes import *
from models import *


with app.app_context():
    db.create_all()
app.run()


