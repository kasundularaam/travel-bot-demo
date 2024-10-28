import pandas as pd
import numpy as np
from datetime import datetime


class TravelBotData:
    def __init__(self):
        # Load CSV files
        self.flights = pd.read_csv('data/flights.csv')
        self.bookings = pd.read_csv('data/bookings.csv')
        self.users = pd.read_csv('data/users.csv')

    def search_flights(self, departure_city, arrival_city, departure_date, class_type='economy'):
        """Search for available flights based on criteria"""
        available_flights = self.flights[
            (self.flights['departure_city'] == departure_city) &
            (self.flights['arrival_city'] == arrival_city) &
            (self.flights['departure_date'] == departure_date) &
            (self.flights['class_type'] == class_type) &
            (self.flights['seats_available'] > 0)
        ]
        return available_flights

    def create_booking(self, flight_id, user_id, passenger_count):
        """Create a new booking"""
        # Get flight details
        flight = self.flights[self.flights['flight_id'] == flight_id].iloc[0]

        # Calculate total price
        total_price = flight['price'] * passenger_count

        # Create booking record
        new_booking = {
            'booking_id': f'BK{len(self.bookings) + 1:03d}',
            'flight_id': flight_id,
            'user_id': user_id,
            'booking_date': datetime.now().strftime('%Y-%m-%d'),
            'passenger_count': passenger_count,
            'total_price': total_price,
            'status': 'confirmed'
        }

        # Add to bookings and save
        self.bookings = pd.concat([self.bookings, pd.DataFrame([new_booking])])
        self.bookings.to_csv('data/bookings.csv', index=False)

        # Update available seats
        self.flights.loc[self.flights['flight_id'] ==
                         flight_id, 'seats_available'] -= passenger_count
        self.flights.to_csv('data/flights.csv', index=False)

        return new_booking['booking_id']

    def get_user_bookings(self, user_id):
        """Get all bookings for a user"""
        user_bookings = self.bookings[self.bookings['user_id'] == user_id]
        return user_bookings
