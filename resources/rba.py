from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify,request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import RBA
from schemas import PlainBook1Schema,PlainBookSchema, PlainRba1Schema,PlainRbaSchema,role_schema
import json
from marshmallow import ValidationError
from sqlalchemy.types import JSON

from sqlalchemy.dialects.postgresql import array
from sqlalchemy.dialects import postgresql
from sqlalchemy import select, func,asc

blp = Blueprint("Roles", "Roles", description="Operations on Roles")

@blp.route("/role")
class Role(MethodView):
    def get(self):
        data= RBA.query.first()
        print(data)
        if data is None:

            role = RBA(name="Super Admin",active=True,role={"user_management" : True, "account_management":True,"store_management":True, "support_management" : True})
        # example2 = Example(json_column={"key" : "newvalue", "myarray" : [23, 676, 45, 88, 99], "objects" : {"name" : "Brian"}})
            db.session.add(role)
            db.session.commit()
       

        return " Role Create succesfully"

    @blp.arguments(PlainRbaSchema)
    # @blp.response(201, PlainRba1Schema)
    def post(self,store_data):
        data= RBA.query.first()
        name=store_data['name']
        active=store_data['active']
        user_management=store_data['user_management']
        account_management=store_data['account_management']
        store_management=store_data['store_management']
        support_management=store_data['support_management']
        
        if data is not None:

            role = RBA(name=name,active=active,role={"user_management" : user_management , "account_management":account_management ,"store_management":store_management , "support_management" : support_management})
        # example2 = Example(json_column={"key" : "newvalue", "myarray" : [23, 676, 45, 88, 99], "objects" : {"name" : "Brian"}})
            db.session.add(role)
            db.session.commit()
           

            return " Role Create succesfully",201
        else:
            return "First Role is Already created"

    


@blp.route('/roles', methods=['GET'])
def get_all_roles():
    users = RBA.query.order_by(asc(RBA.id)).all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['active'] = user.active
        user_data['role'] = user.role
       
        output.append(user_data)

    return jsonify({'roles' : output})


@blp.route('/role/<role_id>', methods=['GET'])
def get_one_role_by_id(role_id):
    data = RBA.query.filter_by(id=role_id).first()

    if not data:
        return jsonify({'message' : 'No role found!'})

    output_data = {}
    output_data['id'] = data.id
    output_data['name'] = data.name
    output_data['active'] = data.active
    output_data['role'] = data.role

    return jsonify(output_data)


@blp.route('/role/<role_id>', methods=['PUT'])

def get_update_role_by_id(role_id):
    data = RBA.query.filter_by(id=role_id).first()
    print(data.active)
    if data is not None:
        if (request.data):
            json_data=request.get_json()
            if not json_data:
                return {"message": "No input data provided"}, 400
            try:
                request_data = role_schema.load(json_data)
                print(request_data)
                role = RBA(name=data.name,active=data.active,role=request_data)
                print(role,'......../../.././/./.')
            # example2 = Example(json_column={"key" : "newvalue", "myarray" : [23, 676, 45, 88, 99], "objects" : {"name" : "Brian"}})
                db.session.add(role)
                db.session.commit()
                # print(request_data)
                # print(request_data['account_management'])
                # print(request_data['store_management'])
                return "update Sucessfuly"
            except ValidationError as err:
                return err.messages, 422
        else:
            return "to request has not data",400

    if not data:
        return jsonify({'message' : 'No role found!'})

    # output_data = {}
    # output_data['id'] = data.id
    # output_data['name'] = data.name
    # output_data['active'] = data.active
    # output_data['role'] = data.role
    # user_management= data.role["user_management"]
    # store_management= data.role["store_management"]
    # support_management= data.role["support_management"]
    # account_management= data.role["account_management"]
    # print(user_management,store_management,support_management,account_management)

    # return jsonify(output_data)

  
        # example1 = Example(json_column={"key" : "value", "myarray" : [39, 323, 83, 382, 102], "objects" : {"name" : "Anthony"}})

        # users =  Example.query.first()
        # users = db.session.query(Example).filter(Example.id==4).first()
        # x="mak"
        # print(users.json_column)
        # lol=[]
        # id = users.id
        # key=users.json_column["key"]
        # myarray=users.json_column["myarray"]
        # objects=users.json_column["objects"]
        # name=users.json_column["objects"]['name']
        # print(id)
        # print(key)
        # print(myarray)
        # print(type(myarray))
        # print(objects)
        # print(name)
        # myarray.insert(0,1111)
        # print(myarray,'//')
        # # user_data['name'] = users.json_column['objects']['name']          objects name change
        # # users.json_column={"key":key,"myarray":myarray,"objects":{"name":"nazmul"}}  # only name filed change
        # # users.json_column={"key":key,"myarray":myarray,"objects":{"name":name}}  # only array filed value add
        # print(users.json_column,'..............')
        # user = Example.query.filter(Example.id==4).update({"json_column":{"key":key,"myarray":myarray,"objects":{"name":name}}})
        # print(user)
        # print(users.json_column['objects']['name'])
        # print(users.book_info,'////')
        # user_data['name'] ="abdullah"

        # output = []
        
        # output.append(user_data)
        # db.session.add(users)
        # db.session.commit()

        # return "update sucvcesfully"

    # @blp.response(200, PlainExampleSchema())
    # def get(self):
    #     dbdata= Example.query.first()
    #     print(dbdata.json_column)
        
    #     x=dbdata.json_column
    #     print(type(x))
    #     lol=json.dumps(x)
    #     y=str(x)
    #     print(type(x),'xxxxxxxxxxxxxxxxxxxxxx')
    #     print(x,'xxxxxxxxxxxxxxxxxxxxxx')
    #     print(type(y),'yyyyyyyyyyyyyyyyyyyyyy')
    #     print(y,'yyyyyyyyyyyyyyyyyyyyyy')
    #     print(x)
    #     data2 = json.dumps(y)
    #     data3 = json.loads(data2)
    #     print(data3,'222222222')
    #     return lol

    # def put(self):

    #     jsonData = '{"ID":"123", "Name": "Hamza"}'
    #     data = json.loads(jsonData)
    #     print(type(data))
    #     newData = {"DOB": "22-10-2001"}
    #     data.update(newData)
    #     print(data)
        
    #     return jsonify({'message' : 'The user has been promoted!'})


    # def put(self):
    #     # example1 = Example(json_column={"key" : "value", "myarray" : [39, 323, 83, 382, 102], "objects" : {"name" : "Anthony"}})

    #     # users =  Example.query.first()
    #     users = db.session.query(Example).filter(Example.id==4).first()
    #     # x="mak"
    #     print(users.json_column)
    #     lol=[]
    #     id = users.id
    #     key=users.json_column["key"]
    #     myarray=users.json_column["myarray"]
    #     objects=users.json_column["objects"]
    #     name=users.json_column["objects"]['name']
    #     print(id)
    #     print(key)
    #     print(myarray)
    #     print(type(myarray))
    #     print(objects)
    #     print(name)
    #     # myarray.insert(0,107)
    #     print(myarray,'//')
    #     # user_data['name'] = users.json_column['objects']['name']          objects name change
    #     users.json_column={"key":key,"myarray":myarray,"objects":{"name":"nazmul"}}  # only name filed change
    #     # users.json_column={"key":key,"myarray":myarray,"objects":{"name":name}}  # only array filed value add
    #     print(users.json_column,'..............')
    #     users = db.session.update(Example).filter(Example.id==4).first()
    #     # print(users.json_column['objects']['name'])
    #     # print(users.book_info,'////')
    #     # user_data['name'] ="abdullah"

    #     # output = []
        
    #     # output.append(user_data)
    #     db.session.add(users)
    #     db.session.commit()

    #     return "update sucvcesfully"

        
        
    # def put(self):
    #     # example1 = Example(json_column={"key" : "value", "myarray" : [39, 323, 83, 382, 102], "objects" : {"name" : "Anthony"}})

    #     # users =  Example.query.first()
    #     users = db.session.query(Example).filter(Example.id==4).first()
    #     # x="mak"
    #     print(users.json_column)
    #     lol=[]
    #     id = users.id
    #     key=users.json_column["key"]
    #     myarray=users.json_column["myarray"]
    #     objects=users.json_column["objects"]
    #     name=users.json_column["objects"]['name']
    #     print(id)
    #     print(key)
    #     print(myarray)
    #     print(type(myarray))
    #     print(objects)
    #     print(name)
    #     myarray.insert(0,1111)
    #     print(myarray,'//')
    #     # user_data['name'] = users.json_column['objects']['name']          objects name change
    #     # users.json_column={"key":key,"myarray":myarray,"objects":{"name":"nazmul"}}  # only name filed change
    #     # users.json_column={"key":key,"myarray":myarray,"objects":{"name":name}}  # only array filed value add
    #     print(users.json_column,'..............')
    #     user = Example.query.filter(Example.id==4).update({"json_column":{"key":key,"myarray":myarray,"objects":{"name":name}}})
    #     print(user)
    #     # print(users.json_column['objects']['name'])
    #     # print(users.book_info,'////')
    #     # user_data['name'] ="abdullah"

    #     # output = []
        
    #     # output.append(user_data)
    #     # db.session.add(users)
    #     db.session.commit()

    #     return "update sucvcesfully"

        