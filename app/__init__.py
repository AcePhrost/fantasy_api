from flask import Flask

app = Flask(__name__)

from resources.players import bp as player_bp

app.register_blueprint(player_bp)

from resources.users import bp as user_bp

app.register_blueprint(user_bp)