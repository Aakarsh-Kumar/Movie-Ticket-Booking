from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.theater_routes import theater_routes
    from app.routes.screen_routes import screen_routes
    from app.routes.movie_routes import movie_routes
    from app.routes.booking_routes import booking_routes
    from app.routes.food_routes import food_routes
    from app.routes.user_routes import user_routes
    from app.routes.cancel_booking_routes import cancel_booking_routes

    app.register_blueprint(theater_routes, url_prefix='/')
    app.register_blueprint(screen_routes, url_prefix='/')
    app.register_blueprint(movie_routes, url_prefix='/')
    app.register_blueprint(booking_routes, url_prefix='/')
    app.register_blueprint(food_routes, url_prefix='/')
    app.register_blueprint(user_routes, url_prefix='/')
    app.register_blueprint(cancel_booking_routes, url_prefix='/')

    return app
