from flask_restx import Resource, Namespace
from flask import request
from setup_db import db
from models import Director, DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        directors = db.session.query(Director).all()
        return directors_schema.dump(directors), 200

@director_ns.route ('/<int:did>')
class DirectorView (Resource):
    def get(self, did):
        director = Director.query.get(did)
        return director_schema.dump(director), 200


