from flask import Blueprint, request, jsonify
from app.models import db, Booking
from pickle import loads,dumps
from requests import post
from datetime import datetime

cancel_booking_routes = Blueprint('cancel_booking_routes', __name__)

@cancel_booking_routes.route('/cancel-booking', methods=['POST'])
def cancel_booking():
    data = request.json
    booking_id = data.get('booking_id')
    booking = Booking.query.get(booking_id)
    if booking is None:
        return jsonify({'message': 'Booking not found'}), 404
    #checking time



    movie = booking.movie

    #checking time window
    show_time = movie.show_time
    if not (show_time-datetime.now()).total_seconds()>1800:
        return jsonify({'message': 'Cancellation closed'})
    #update the movie's booked seats
    booked_seats = loads(movie.booked_seats)
    for seat in loads(booking.seats_booked):
        booked_seats.remove(seat)
    movie.booked_seats = dumps(booked_seats)
    db.session.delete(booking)
    update_waiting_list(booking.movie)
    
    return jsonify({'message': 'Booking cancelled successfully'}), 200

def update_waiting_list(movie):
    waiting_list = movie.waiting_list
    if waiting_list:
        waiting_list = waiting_list[0]
        waiting_seats = waiting_list.seats_requested
        if waiting_seats <= updated_booking_count:
            waiting_list.delete()
            updated_booking_count += waiting_seats
            movie.booking_count = updated_booking_count
            post('http://localhost:5000/bookings', json={
                'user_id': waiting_list.user_id,
                'movie_id': waiting_list.movie_id,
                'seats_requested': waiting_seats,
                'food_items': waiting_list.food_items
            })
    db.session.commit()
    
    