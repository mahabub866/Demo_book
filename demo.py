# from flask import Flask ,current_app
# from flask_sqlalchemy import SQLAlchemy 
# from sqlalchemy.dialects.postgresql import JSON

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/demo_json'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy(app)


# class Example(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     json_column = db.Column(JSON)






# # with app.app_context():
# #     db.create_all()

    
# def insert_data():
    # example1 = Example(json_column={"key" : "value", "myarray" : [39, 323, 83, 382, 102], "objects" : {"name" : "Anthony"}})
#     example2 = Example(json_column={"key" : "newvalue", "myarray" : [23, 676, 45, 88, 99], "objects" : {"name" : "Brian"}})
#     db.session.add(example2)
#     db.session.commit()

# insert_data()
# # with app.app_context():
# #     print(current_app.name)

# # def query():
# #     #example1 = Example.query.first()
# #     #print(example1)
# #     #print(example1.json_column['myarray'][4])
# #     #print(type(example1.json_column))
# #     results = Example.query.filter(Example.json_column['objects']['name'].astext == 'Brian').all()
# #     print(results)

# # query()