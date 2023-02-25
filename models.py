# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)
from marshmallow import Schema, fields

from setup_db import db

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column (db.String)
    trailer = db.Column (db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column (db.Integer, db.ForeignKey ("genre.id"))
    genre = db.relationship ("Genre")
    director_id = db.Column (db.Integer, db.ForeignKey ("director.id"))
    director = db.relationship ("Director")

class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float( )
    genre_id = fields.Int( )
    director_id = fields.Int()

class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class Director(db.Model):
    __tablename__ = "director"
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String)

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()




