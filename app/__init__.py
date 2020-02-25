from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# automatically redirect the user to the login form, and only redirect back to the page the user wanted to view
# after the login process is complete.
login.login_view = 'login'

# this bottom impoort is a workaround to circular imports. 'routes' module needs to import the app variable defined in this script
from app import routes, models
