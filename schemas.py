from marshmallow import Schema , fields

class User(Schema):
    id = fields.Str(dump_only = True)
    email = fields.Str(dump_only = True)