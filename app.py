# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение


from flask import Flask
from flask_restx import Api

from config import Config
from models import Movie, Director, Genre
from setup_db import db
from views.movie import movie_ns
from views.director import director_ns
from views.genre import genre_ns

#функция создания основного объекта app
def create_app(config):
     app = Flask(__name__)
     app.config.from_object(config)
     app.app_context().push()
     return app

def create_data(application, db):
    with application.app_context():
        db.create_all()

# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application: Flask):
     db.init_app(application)
     api = Api(application)
     api.add_namespace(movie_ns)
     api.add_namespace (director_ns)
     api.add_namespace (genre_ns)
     create_data(application, db)

app_config = Config()
application = create_app(app_config)
register_extensions(application)

#app = create_app(Config())
#app.debug = True

if __name__ == '__main__':
    app_config = Config ( )
    application = create_app (app_config)
    register_extensions (application)
    application.run(debug=True)



