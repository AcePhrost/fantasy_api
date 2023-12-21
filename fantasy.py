from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

user = {
    '1': {
        'username': 'Phrost',
        'email': 'Camo@mail'
    },

    '2': {
        'username': 'Ace',
        'email': 'something@mail'
    }

}

players = {
    '1': {
        'first_name': 'Josh',
        'last_name': 'Allen',
        'position': 'Quaterback'
    },
    '2': {
        'first_name': 'Jalen',
        'last_name': 'Hurts',
        'position': 'Quaterback'
    }
}

# roster = {
#     '1': {
#         'position_id': '1',
#         'user_id': '1'
#     },

#     '2': {
#         'position_id': '2',
#         'user_id': '2'
#     }
# }

@app.get('/player')
def player():
    return { 'players': list(players.values()) }

@app.get('/user')
def users():
    return { 'users': list(user.values())} ,200

@app.route('/user', methods=['POST'])
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return {'message' : f'{json_body['username']} created' }, 201

@app.delete('/player/<player_id>')
def del_player(player_id):
    try:
        del players[player_id]
        return {'message': f'{player_id} has been deleted'}
    except: 
        return {'message': 'Player not found'}

