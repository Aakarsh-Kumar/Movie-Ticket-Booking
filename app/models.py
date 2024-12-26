from . import db
from datetime import datetime
from pickle import dumps

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

class Theater(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    screens = db.relationship('Screen', backref='theater', lazy=True)
    

class Screen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.PickleType, nullable=False)
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'), nullable=False)
    movies = db.relationship('Movie', backref='screen', lazy=True)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.id'), nullable=False)
    show_time = db.Column(db.DateTime, nullable=False)
    booked_seats = db.Column(db.PickleType, default=dumps([]))
    bookings = db.relationship('Booking', backref='movie', lazy=True)
    waiting_list = db.relationship('WaitingList', backref='movie', lazy=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    seats_booked = db.Column(db.PickleType, nullable=False)
    food_items = db.Column(db.PickleType,  db.ForeignKey('food.id'),default=dumps([]))
    booked_at = db.Column(db.DateTime, default=datetime.now)

class WaitingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    seats_requested = db.Column(db.Integer, nullable=False)
    food_items = db.Column(db.PickleType, nullable=True)
    added_at = db.Column(db.DateTime, default=datetime.now)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bookings = db.relationship('Booking', backref='food', lazy=True)

