from flask import Flask

app = Flask(__name__)

# this bottom impoort is a workaround to circular imports. 'routes' module needs to import the app variable defined in this script
from app import routes
