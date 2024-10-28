from travel_bot_data import TravelBotData
from datetime import datetime
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class TravelBot:
    def __init__(self):
        self.data_handler = TravelBotData()
        self.current_user = None
        self.context = {}
        self.conversation_state = "GREETING"

        # Initialize intent patterns
        self.intent_patterns = {
            'greeting': [r'hi|hello|hey', r'good (morning|afternoon|evening)'],
            'book_flight': [r'book( a)? flight', r'need( a)? ticket', r'want to travel'],
            'search_flights': [r'search flights?', r'find flights?', r'check flights?'],
            'check_booking': [r'check( my)? booking', r'booking status', r'my tickets?'],
            'cancel_booking': [r'cancel( my)? booking', r'cancel ticket'],
            'farewell': [r'bye|goodbye|thank you|thanks']
        }

    def detect_intent(self, user_input):
        """Detect user intent from input"""
        user_input = user_input.lower()

        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input):
                    return intent

        return "unknown"

    def extract_entities(self, user_input):
        """Extract relevant entities from user input"""
        entities = {}

        # Example city extraction (you can expand this)
        cities = ['london', 'paris', 'new york', 'tokyo']  # Add more cities
        words = user_input.lower().split()

        for city in cities:
            if city in words:
                if 'from' in words and words.index(city) > words.index('from'):
                    entities['departure_city'] = city.title()
                elif 'to' in words and words.index(city) > words.index('to'):
                    entities['arrival_city'] = city.title()

        # Example date extraction
        date_pattern = r'(\d{2}(/|-)\d{2}(/|-)\d{4})'
        dates = re.findall(date_pattern, user_input)
        if dates:
            entities['date'] = dates[0][0]

        return entities

    def handle_greeting(self):
        if self.current_user:
            return f"Welcome back! How can I help you today?"
        return "Welcome to Travel Booking Assistant! How can I help you today?"

    def handle_flight_search(self, user_input):
        entities = self.extract_entities(user_input)

        if not entities.get('departure_city') or not entities.get('arrival_city'):
            return "I need both departure and arrival cities. Please specify them."

        if not entities.get('date'):
            return "Please specify your travel date (DD/MM/YYYY)."

        flights = self.data_handler.search_flights(
            departure_city=entities['departure_city'],
            arrival_city=entities['arrival_city'],
            departure_date=entities['date']
        )

        if flights.empty:
            return "Sorry, no flights found for your criteria."

        # Format flight results
        response = "Here are the available flights:\n\n"
        for _, flight in flights.iterrows():
            response += (f"Flight {flight['flight_id']}:\n"
                         f"From {flight['departure_city']} to {
                             flight['arrival_city']}\n"
                         f"Date: {flight['departure_date']} "
                         f"(Departure: {flight['departure_time']}, "
                         f"Arrival: {flight['arrival_time']})\n"
                         f"Price: £{
                             flight['price']:.2f} ({flight['class_type']} class)\n"
                         f"Seats available: {flight['seats_available']}\n\n")

        return response

    def process_input(self, user_input):
        """Process user input and generate response"""
        intent = self.detect_intent(user_input)

        # Handle different intents
        if intent == "greeting":
            return self.handle_greeting()

        elif intent == "search_flights":
            return self.handle_flight_search(user_input)

        elif intent == "book_flight":
            if "BOOKING" not in self.conversation_state:
                self.conversation_state = "BOOKING_INIT"
                return "Sure! I can help you book a flight. Where would you like to fly from?"

        elif intent == "check_booking":
            if not self.current_user:
                return "Please log in first to check your bookings."
            bookings = self.data_handler.get_user_bookings(self.current_user)
            if bookings.empty:
                return "You don't have any bookings."
            return self.format_bookings(bookings)

        elif intent == "farewell":
            return "Thank you for using our service. Have a great day!"

        return "I'm not sure what you're asking for. Could you please rephrase that?"

    def format_bookings(self, bookings):
        """Format booking information for display"""
        response = "Here are your bookings:\n\n"
        for _, booking in bookings.iterrows():
            response += (f"Booking ID: {booking['booking_id']}\n"
                         f"Flight: {booking['flight_id']}\n"
                         f"Date: {booking['booking_date']}\n"
                         f"Passengers: {booking['passenger_count']}\n"
                         f"Total price: £{booking['total_price']:.2f}\n"
                         f"Status: {booking['status']}\n\n")
        return response
