# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask_restx import Resource, Namespace
from flask import request
from setup_db import db
from models import Movie, MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        gid = request.args.get ('genre_id')
        did = request.args.get ('director_id')
        year = request.args.get ('year')
        mdg = Movie.query
        if did:
            mdg = mdg.filter (Movie.director_id == did)
        if gid:
            mdg = mdg.filter (Movie.genre_id == gid)
        if year:
            mdg = mdg.filter (Movie.year == year)

        movies = mdg.all()
        return movies_schema.dump(movies), 200
    def post(self) :
        data = request.json
        new_movie = Movie(**data)
        db.session.add(new_movie)
        db.session.commit()
        return '', 201

@movie_ns.route ('/<int:mid>')
class MovieView (Resource):
    def get(self, mid):
        movie = Movie.query.get(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        movie = Movie.query.get (mid)
        if not movie:
            return "", 404
        req_json = request.json
        movie.name = req_json.get ('name')
        movie.title = req_json.get ('title')
        movie.description = req_json.get ('description')
        movie.trailer = req_json.get ('trailer')
        movie.year = req_json.get ('year')
        movie.rating = req_json.get ('rating')
        db.session.add (movie)
        db.session.commit()
        return "", 204

    def delete(self, mid):
        movie = Movie.query.get (mid)
        if not movie:
            return "", 404
        db.session.delete(movie)
        db.session.commit()
        return "", 204


