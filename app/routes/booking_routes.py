from flask import Blueprint, request, jsonify
from app.models import db, Booking, Movie,Screen, Food, WaitingList
from pickle import loads, dumps

booking_routes = Blueprint('booking_routes', __name__)

@booking_routes.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    seats_requested = int(data.get('seats_requested'))
    food_items = data.get('food_items', []) 
    total_seats = len(loads(Screen.query.get(Movie.query.get(movie_id).screen_id).seats))
    booked_seats_count = len(loads(Movie.query.get(movie_id).booked_seats))
    if total_seats - booked_seats_count < seats_requested:
        add_waiting()
        return jsonify({'message': 'Seats not available. Added to waiting list'})
    alloted_seats = allot_seats(movie_id, seats_requested)
    new_booking = Booking(user_id=user_id, movie_id=movie_id, seats_booked=dumps(alloted_seats), food_items=dumps(food_items))
    db.session.add(new_booking)
    
    movie = Movie.query.get(movie_id)
    movie.booked_seats = dumps(loads(movie.booked_seats) + alloted_seats)
    db.session.commit()
    
    return jsonify({
        'id': new_booking.id,
        'user_id': new_booking.user_id,
        'movie_id': new_booking.movie_id,
        'seats_booked': loads(new_booking.seats_booked),
        'food_items': loads(new_booking.food_items),
        'booked_at': new_booking.booked_at
    })

@booking_routes.route('/api/amount', methods=['POST'])
def get_amount():
    data = request.json
    movie_id = data.get('movie_id')
    seats_requested = int(data.get('seats_requested'))
    food_items = data.get('food_items', [])
    
    ticket_total = Movie.query.get(movie_id).screen.price * seats_requested
    food_total = sum([Food.query.get(food_item).price for food_item in food_items])
    total_amount = ticket_total + food_total
    return jsonify({'total_amount': total_amount, 'ticket_total': ticket_total, 'food_total': food_total})

def add_waiting():
    data = request.json
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    seats_requested = int(data.get('seats_requested'))
    food_items = data.get('food_items', [])
    new_waiting = WaitingList(user_id=user_id, movie_id=movie_id, seats_requested=seats_requested, food_items=dumps(food_items))
    db.session.add(new_waiting)
    db.session.commit()
    return jsonify({
        'id': new_waiting.id,
        'user_id': new_waiting.user_id,
        'movie_id': new_waiting.movie_id,
        'seats_requested': new_waiting.seats_requested,
        'food_items': loads(new_waiting.food_items)
    })

def allot_seats(movie_id, seats_requested):
    movie = Movie.query.get(movie_id)
    screen = Screen.query.get(movie.screen_id)
    booked_seats = loads(movie.booked_seats)
    alloted_seats = []
    for seat in range(1, len(loads(screen.seats)) + 1):
        if seat not in booked_seats:
            alloted_seats.append(seat)
            if len(alloted_seats) == seats_requested:
                break
    return alloted_seats