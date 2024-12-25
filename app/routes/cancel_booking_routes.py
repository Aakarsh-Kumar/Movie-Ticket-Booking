from flask import Blueprint, request, jsonify
from app.models import db, Booking
from pickle import loads

cancel_booking_routes = Blueprint('cancel_booking_routes', __name__)

@cancel_booking_routes.route('/cancel-booking', methods=['POST'])
def cancel_booking():
    data = request.json
    booking_id = data.get('booking_id')
    booking = Booking.query.get(booking_id)
    if booking is None:
        return jsonify({'message': 'Booking not found'}), 404
    seats_booked = len(loads(booking.seats_booked))
    db.session.delete(booking)
    updated_booking_count = booking.movie.booking_count - seats_booked
    booking.movie.booking_count = updated_booking_count
    db.session.commit()

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
            #we need to create a booking with the details in the waiting list
            # new_booking = Booking(user_id=waiting_list.user_id, movie_id=waiting_list.movie_id, seats_booked=, food_items=waiting_list.food_items)
            db.session.commit()
    
    