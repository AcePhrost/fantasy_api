from flask import Flask

app = Flask(__name__)

from resources.Players import routes
from resources.Users import routes