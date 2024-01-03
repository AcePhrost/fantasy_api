from flask_smorest import Blueprint

bp = Blueprint('players', __name__, description= 'Operation for players', url_prefix= '/player')

from . import routes