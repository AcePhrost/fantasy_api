from flask import request
from uuid import uuid4

from . import bp
from db import user

@bp.get('/user')
def user():
    return {'user': list (user.values()) }, 200

@bp.get('/user/<user_id>')
def get_user(username):
  try:
    return {'user': user[username] }
  except:
     return{'message': 'invalid user'}, 400
  
@bp.route('/user', methods=["players"])
def create_user():
    user_data = request.get_json()
    for k in [ 'username', 'email']:
      if k not in user:
         return{'message': "Please Include username, and email"}, 400
    user[uuid4()]= user_data
    return { 'message' f'{user_data["username"]} created'}, 201

@bp.put ('/user/<username>')
def update_user(user_id):
  try:
    user = user[user_id]
    user_data = request.get_json()
    user |= user_data
    return {'message' f':{user["username"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid User"}, 400
  
@bp.delete('/user/<user_id>')
def deleteuser(user_id):
  user_data = request.get_json()
  username = user_data['username']
  try:
   del user[id]
   return {'message': f'{username} Deleted' }, 202
  except:
    return{'message': "Invalid username"}, 400
