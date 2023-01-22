from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema

class PlainBookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Boolean(required=True)
    # created_at = fields.DateTime()
    rating=fields.Str(required=True)
    user_number=fields.Str(required=True)
    book_info = JSONSchema()
    

class PlainBook1Schema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Boolean(required=True)
    # created_at = fields.DateTime()
    book_info = fields.Str()

class PlainExampleSchema(Schema):
    id = fields.Int(dump_only=True)
    json_column = fields.Str()
    
class BookRatingUpdateSchema(Schema):
   
    name = fields.Str()
    status = fields.Boolean()
    # created_at = fields.DateTime()
    rating=fields.Str()
    user_number=fields.Str()
    book_info = JSONSchema()
    id = fields.Int()
    