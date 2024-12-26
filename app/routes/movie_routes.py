from flask import Blueprint, jsonify, request
from app.models import db, Movie
import datetime
from pickle import loads, dumps

movie_routes = Blueprint('movie_routes', __name__)

@movie_routes.route('/movies', methods=['GET'])
def get_movies():   
    movies = Movie.query.all()
    return jsonify([
        {
            'id': movie.id,
            'name': movie.name,
            'description': movie.description,
            'duration':movie.duration,
            'screen_id':movie.screen_id,
            'show_time':movie.show_time,
            'booked_seats':loads(movie.booked_seats)
        }
        for movie in movies
    ])


@movie_routes.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    duration = data.get('duration')
    screen_id = data.get('screen_id')
    show_time = datetime.datetime.strptime(data.get('show_time'), '%d-%m-%Y %H:%M')
    new_movie = Movie(name=name, description=description, duration=duration, screen_id=screen_id, show_time=show_time)
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({
        'id': new_movie.id,
        'name': new_movie.name,
        'description': new_movie.description,
        'duration': new_movie.duration,
        'screen_id': new_movie.screen_id,
        'show_time': new_movie.show_time,
        'booked_seats': loads(new_movie.booked_seats)
    })

@movie_routes.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get_or_404(id)
    return jsonify({
        'id': movie.id,
        'name': movie.name,
        'description': movie.description,
        'duration': movie.duration,
        'screen_id': movie.screen_id,
        'show_time': movie.show_time,
        'booked_seats':loads(movie.booked_seats),
        'seats':loads(movie.screen.seats)
    })
