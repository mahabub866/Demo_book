from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import secrets
from db import db
import os
import models
from dotenv import load_dotenv
import psycopg2
# last e install dibo
from flask_migrate import Migrate
from blocklist import BLOCKLIST
from resources.book import blp as BookBlueprint
from resources.demo import blp as ExamplesBlueprint
# from resources.store import blp as StoreBlueprint
# from resources.tag import blp as TagBlueprint
# from resources.user import blp as UserBlueprint
# from resources.test import blp as TestBlueprint
from datetime import datetime, timedelta

def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    # url=os.getenv("DATABASE_URL")
    # connection=psycopg2.connect(url)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/Demo"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/Demo"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/book_demo'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/book_demo'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/book_demo"
    # app.config["SQLALCHEMY_DATABASE_URI"] = connection
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    #  this code must be written this place
    migrate = Migrate(app, db)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "Mahabub27dec1997!7276mahabub866!127866"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    # app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128)
    jwt = JWTManager(app)



# 
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    # @jwt.additional_claims_loader
    # def add_claims_to_jwt(identity):
    #     if identity == 1:
    #         return {"is_admin": True}
    #     return {"is_admin": False}
        
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )



    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    with app.app_context():
        db.create_all()

    api.register_blueprint(BookBlueprint)
    api.register_blueprint(ExamplesBlueprint)
    # api.register_blueprint(TagBlueprint)
    # api.register_blueprint(UserBlueprint)
    # api.register_blueprint(TestBlueprint)

    return app