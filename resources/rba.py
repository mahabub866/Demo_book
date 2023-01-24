from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify,request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import RBA
from schemas import role_schema_main,PlainBookSchema, PlainRba1Schema,PlainRbaSchema,role_schema,role_status_schema
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

    

@blp.route('/get-role', methods=['POST'])
def get_role():

    if (request.data):
            json_data=request.get_json()
            
            if not json_data:
                return {"message": "No input data provided"}, 400
            try:
                request_data = role_schema_main.load(json_data)
                data = RBA.query.filter_by(name=request_data['name']).first()
                # print(data,'data')
                if data:
                    return {"message": "Name Already Exist"}, 422
                
                print(request_data['active'])
                print(request_data)
                role = RBA(name=request_data['name'],active=request_data['active'],role={"user_management" : request_data['user_management']  , "account_management":request_data['account_management'] ,"store_management":request_data['store_management'] , "support_management" : request_data['support_management']})
                # role = request_data

                # print(role)

                db.session.add(role)
                db.session.commit()
               
                return "Create Succesfully"
            except ValidationError as err:
                return err.messages, 422
    else:
        return "This request has not data",400
    
    
 
        

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
    if not data:
        return jsonify({'message' : 'No role found!'})
    else:
        if (request.data):
            json_data=request.get_json()
            if not json_data:
                return {"message": "No input data provided"}, 400
            try:
                request_data = role_schema.load(json_data)
                print(request_data)
                # role = RBA(name=data.name,active=data.active,role=request_data)
                user = RBA.query.filter(RBA.id==role_id).update({"role":request_data})
                # print(user,'......../../.././/./.')
            
                db.session.commit()
               
                return "update Sucessfuly"
            except ValidationError as err:
                return err.messages, 422
        else:
            return "This request has not data",400


@blp.route('/role/status/<role_id>', methods=['PUT'])
def role_status_update( role_id):
    data =  data = RBA.query.filter_by(id=role_id).first()

    if not data:
        return jsonify({'message' : 'No role found!'})
    else:
        if (request.data):
            json_data=request.get_json()
            print(json_data)

            if not json_data:
                return {"message": "No input data provided"}, 400
            try:
                request_data = role_status_schema.load(json_data)
                print(request_data["active"])
        #         # role = RBA(name=data.name,active=data.active,role=request_data)
                user = RBA.query.filter(RBA.id==role_id).update({"active":request_data['active']})
                # print(user,'......../../.././/./.')
            
                db.session.commit()
               
                return "update Sucessfuly"
            except ValidationError as err:
                return err.messages, 422
        else:
            return "This request has not data",400


@blp.route('/todo/<role_id>', methods=['DELETE'])

def delete_role( role_id):
    role = RBA.query.filter_by(id=role_id).first()

    if not role:
        return jsonify({'message' : 'No role found!'})

    db.session.delete(role)
    db.session.commit()

    return jsonify({'message' : 'role  deleted Succesfully!'})