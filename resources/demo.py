
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import Example
from schemas import PlainExampleSchema,PlainBookSchema,BookRatingUpdateSchema
import json
from sqlalchemy.types import JSON

from sqlalchemy.dialects.postgresql import array
from sqlalchemy.dialects import postgresql
from sqlalchemy import select, func

blp = Blueprint("Examples", "Examples", description="Operations on Examples")




sampleJson = """{"key" : "value", "myarray" : [39, 323, 83, 382, 102], "objects" : {"name" : "Anthony"}}"""
@blp.route("/example")
class demo(MethodView):
    # def get(self):
    #     example1 = Example(json_column={"key" : "value", "myarray" : [39, 323, 83, 382, 102], "objects" : {"name" : "Anthony"}})
        # example2 = Example(json_column={"key" : "newvalue", "myarray" : [23, 676, 45, 88, 99], "objects" : {"name" : "Brian"}})
    #     db.session.add(example1)
    #     db.session.commit()
    #     return " Complete succesfully"
    # @blp.response(200, PlainExampleSchema())
    def get(self):
        dbdata= Example.query.first()
        print(dbdata.json_column)
        
        x=dbdata.json_column
        print(type(x))
        lol=json.dumps(x)
        y=str(x)
        print(type(x),'xxxxxxxxxxxxxxxxxxxxxx')
        print(x,'xxxxxxxxxxxxxxxxxxxxxx')
        print(type(y),'yyyyyyyyyyyyyyyyyyyyyy')
        print(y,'yyyyyyyyyyyyyyyyyyyyyy')
        print(x)
        data2 = json.dumps(y)
        data3 = json.loads(data2)
        print(data3,'222222222')
        return lol

    def put(self):
        dbdata = Example.query.first()
        x=dbdata.json_column
        y=dbdata.id
        z=x['objects']['name']
        print(x['objects']['name'])
        print(y)
        if x['objects']['name']=="Anthony":
            db.session.update(z="nazmul")
            print(x['objects']['name'])
            db.session.commit()

            print(';lol')
        return x
        
        
        # if y==1:
        #     return x
        #     x=dbdata.json_column
        #     print(x['objects'])
        #     return x
            # p=[]
            # if x['key'] == "value":
                # p=x['key']
                # print(type(p))
               
                # print(p,'...............')
                # db.session.update(p)
                
            
            # db.session.commit()
                
                # print(p)

            # return {"main":p}


    # @blp.response(200, PlainExampleSchema(many=True))
    # def get(self):
    #     dbdata= Example.query.all()
    #     data=[]
    #     for item in dbdata:
    #         print(item.json_column)
    #         x=item.json_column
    #         # print(x)
    #         print(type(x))
    #         lol=json.dumps(x)
    #         # print(lol)
    #     return lol
       
   # def get(self):
    #     data = {"key1" : "value1", "key2" : "value2"}
    #     print(type(data))
    #     jsonData = json.dumps(data)
    #     print(type(sampleJson))
    #     data1 = json.dumps(sampleJson)
    #     data2 = json.loads(sampleJson)
       
            
    #     return jsonify({"dump":data1,"load":data2,'json':jsonData})
        # return dbdata

@blp.route('/user', methods=['GET'])

def get_all_users():
    users = Example.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['json_column'] = user.json_column
       
        output.append(user_data)

    return jsonify({'users' : output})

@blp.route('/single user', methods=['GET'])

def get_all_users():
    users =  Example.query.first()
    # users = db.session.query(Example).first()
    print(users)
    user_data = {}
    user_data['id'] = users.id
    user_data['json_column'] = users.json_column
    output = []
       
    output.append(user_data)

    return jsonify({'users' : output})