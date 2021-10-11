from flask_restful import Resource

import json

from flask import request,abort,jsonify



from src.utils import create_user, find_user_by_id, find_user_by_id_and_delete,find_user_and_update,read_users,update_profile_picture


"""
    controller is about what you want to do with request and response
"""

class UsersHandler(Resource):
    def get(self):
        data = read_users()
        return {'data':json.loads(data)}
    def post(self):
        user = request.get_json()
        new_user = create_user(user)
        return {'data': new_user}

class UserHandler(Resource):
    def get(self,id):
        user = find_user_by_id(id)
        return {'data': json.loads(user)}
    def put(self,id):
        user_to_update = request.get_json()
        user_updated = find_user_and_update(id,user_to_update)
        return {'data': user_updated}
    def post(self,id): ## update profile picture
        file_to_upload = request.files['avatar']
        print(file_to_upload)
        s3_response = update_profile_picture(file_to_upload,id)
        print(s3_response)
        return {'data': "ok"}
    def delete(self,id):
        find_user_by_id_and_delete(id)
        return {'message':"ok" },200