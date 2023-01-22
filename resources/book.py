from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import BookModel
from schemas import PlainBook1Schema,PlainBookSchema,BookRatingUpdateSchema
import json
from sqlalchemy.types import JSON

from sqlalchemy.dialects.postgresql import array
from sqlalchemy.dialects import postgresql
from sqlalchemy import select, func

blp = Blueprint("Books", "books", description="Operations on books")

stmt = array[3,4,5]
@blp.route("/test")
class Test(MethodView):
    @blp.response(200, PlainBook1Schema(many=True))
    def get(self):
        dbdata= BookModel.query.all()
        for item in dbdata:
            print(item.name,'////////////////')
        return dbdata
    # def get(self):
    #     data = []
    #     bdata=[]
    #     cdata=[]
    #     dbdata= BookModel.query.all()
    #     try:
            
                # print(item.text_array)
    #             data=item.book_info
    #             bdata.append(data)
    #     except Exception as e:
    #         print(e)
    #     for item in bdata:
    #         for i in item:
    #             if i['name']=="string":
    #             # print(i['id'])
    #                 print(i['name'])
    #                 print(i['rating'])
    #                 cdata.append({"name":i['name'],"rating":i['rating']})
                    
    #     return jsonify(cdata)
           
    @blp.arguments(BookRatingUpdateSchema)
    @blp.response(200, PlainBook1Schema)
    def put(self, item_data, ):
        books = BookModel.query.all()
        # print(books)
        # print(item_data['id'])
        print(item_data['rating'])

        for item in books:
            if item_data['id']==item.id:
                print(item.book_info)
                item.book_info=[{"name":item_data['name'], "status":item_data['status'],"rating":item_data['rating'],"user_number":item_data['user_number']}]
        db.session.add(item)
        db.session.commit()
        return "Update Sucessfully" 
                # item.price = item_data["price"]
        
        # print(item)
        # if item:
        #     item.price = item_data["price"]
        #     item.name = item_data["name"]
        # else:
        #     item = ItemModel(id=item_id, **item_data)
        #     # abort(400, message="Not found item")

        

          
    @blp.arguments(PlainBookSchema)
    @blp.response(201, PlainBookSchema)
    def post(self, store_data):
       
        name=store_data['name']
        status=store_data['status']
        rating=store_data['rating']
        user_number=store_data['user_number']
        # store = BookModel(name=name,status=status)
        # print(store_data)
        # print(store)
        try:
            store=BookModel(name=name,status=status,book_info=[{"name":name, "status":status,"rating":rating,"user_number":user_number}])
            
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A book with that name already exists.",
            )
        
        

