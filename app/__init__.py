from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# this bottom impoort is a workaround to circular imports. 'routes' module needs to import the app variable defined in this script
from app import routes
