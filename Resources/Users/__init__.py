from flask_smorest import Blueprint

bp = Blueprint('User', __name__, description= 'Operation for Users', )

from . import routes