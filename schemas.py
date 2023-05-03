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

class PlainRba1Schema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    active = fields.Boolean(required=True)
    role = JSONSchema()

class PlainRbaSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    active = fields.Boolean(required=False,default=None)
    user_management=fields.Boolean(required=False,default=None)
    account_management=fields.Boolean(required=False,default=None)
    store_management=fields.Boolean(required=False,default=None)
    support_management=fields.Boolean(required=False,default=None)
    role = JSONSchema()
    

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
    
class RoleUpdateSchema(Schema):
   
    user_management = fields.Boolean(default=None)
    account_management = fields.Boolean(default=None)
    support_management = fields.Boolean(default=None)
    store_management = fields.Boolean(default=None)

class RoleSchema(Schema):
    name=fields.Str()
    active = fields.Boolean(default=False)
    user_management = fields.Boolean(default=None)
    account_management = fields.Boolean(default=None)
    support_management = fields.Boolean(default=None)
    store_management = fields.Boolean(default=None)

class RoleStatusUpdateSchema(Schema):
   
    active = fields.Boolean()
   
    
role_schema=RoleUpdateSchema()
role_schema_main= ()
role_status_schema=RoleStatusUpdateSchema()