from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# você pode definir nomes customizados para pastas com html e css
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from routes import *
from models import *


with app.app_context():
    db.create_all()

# voce definir uma porta com: app.run(port=3000)
app.run()
