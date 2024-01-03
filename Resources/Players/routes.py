from flask import request
from uuid import uuid4

from app import app
from db import user, players



@app.get('/player')
def player():
    return { 'players': list(player.values()) }

@app.get ('/player/<player_id>')
def get_player(player_id):
  try:
    return {'players': players[player_id]}, 200
  except KeyError:
    return {'message': "Invalid Player"}, 400
  
@app.post('/player')
def add_player():
   players_data = request.get_json
   user_id = players_data['user_id']
   if user_id in user:
      players[uuid4()] = players_data
      return {'message': "Player Added" }, 201
   return{'message': "Invalid User"}, 401

@app.put('/player/<player_id>')
def update_player(player_id):
  try:
    Players = player[player_id]
    player_data = request.get_json()
    if player_data['user_id'] == players ['user_id']:
      player['player_id'] = player_data['']
      return {'message': 'Player Updated' }, 202
    return {'message': "Unauthorized"}, 401
  except:
     return {'message': "Invalid Player Id"}, 400
  
@app.delete('/player/<player_id>')
def del_player(player_id):
    try:
        del player[player_id]
        return {'message': f'{player_id} has been deleted'}, 202
    except: 
        return {'message': 'Player not found'}, 400

  