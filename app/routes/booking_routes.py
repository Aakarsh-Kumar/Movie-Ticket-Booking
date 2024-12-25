from flask import Blueprint, request, jsonify
from app.models import db, Booking, Movie,Screen, Food, WaitingList
import pickle

booking_routes = Blueprint('booking_routes', __name__)

@booking_routes.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    seats_requested = int(data.get('seats_requested'))
    food_items = data.get('food_items', []) 
    total_seats = Screen.query.get(Movie.query.get(movie_id).screen_id).seats
    booked_seats = Movie.query.get(movie_id).booking_count
    if total_seats - booked_seats < seats_requested:
        add_waiting()
        return jsonify({'message': 'Seats not available. Added to waiting list'})
    alloted_seats = [allot_seats for allot_seats in range(booked_seats+1, booked_seats+seats_requested+1)]
    new_booking = Booking(user_id=user_id, movie_id=movie_id, seats_booked=pickle.dumps(alloted_seats), food_items=pickle.dumps(food_items))
    Movie.query.get(movie_id).booking_count += seats_requested
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({
        'id': new_booking.id,
        'user_id': new_booking.user_id,
        'movie_id': new_booking.movie_id,
        'seats_booked': pickle.loads(new_booking.seats_booked),
        'food_items': pickle.loads(new_booking.food_items),
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
    new_waiting = WaitingList(user_id=user_id, movie_id=movie_id, seats_requested=seats_requested, food_items=pickle.dumps(food_items))
    db.session.add(new_waiting)
    db.session.commit()
    return jsonify({
        'id': new_waiting.id,
        'user_id': new_waiting.user_id,
        'movie_id': new_waiting.movie_id,
        'seats_requested': new_waiting.seats_requested,
        'food_items': pickle.loads(new_waiting.food_items)
    })
