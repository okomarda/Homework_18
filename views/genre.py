from flask_restx import Resource, Namespace
from flask import request
from setup_db import db
from models import Genre, GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = db.session.query(Genre).all()
        return genres_schema.dump(genres), 200

@genre_ns.route ('/<int:gid>')
class GenreView (Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        return genre_schema.dump(genre), 200