# 🤖 Travel Bot Demo

A simple demonstration of a travel booking chatbot using Natural Language Processing.

## 🚀 Features
- 🔍 Flight search capabilities
- ✈️ Booking management
- 👤 User preference handling
- 💬 Natural language interaction
- 📊 Basic data management

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.12+ 🐍
- Virtual Environment (recommended) 🏠

### 1️⃣ Clone the repository
```bash
git clone https://github.com/kasundularaam/travel-bot-demo.git
cd travel-bot-demo
```

### 2️⃣ Set up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
.\venv\Scripts\activate
# For Unix or MacOS
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download NLTK Data
```bash
python setup_nltk.py
```

### 5️⃣ Verify Setup
```bash
python test_setup.py
```

## 📁 Project Structure
```
travel-bot-demo/
│
├── data/               # CSV data files
│   ├── flights.csv    # Flight information
│   ├── bookings.csv   # Booking records
│   └── users.csv      # User information
│
├── setup_nltk.py      # NLTK setup script
├── test_setup.py      # Environment test script
├── travel_bot_data.py # Data handling class
├── travel_bot.py      # Main chatbot logic
└── main.py           # Entry point
```

## 🎮 Usage
```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate  # Unix/MacOS
# or
.\venv\Scripts\activate  # Windows

# Run the chatbot
python main.py
```

## 💬 Example Interactions
```
User: Hi
Bot: Welcome to Travel Booking Assistant! How can I help you today?

User: I want to book a flight from London to Paris
Bot: When would you like to travel?
...
```

## 📝 Sample Commands
- Search flights: "Show me flights from [city] to [city]"
- Check bookings: "Show my bookings"
- Help: "What can you do?"
- Exit: "quit"

## ⚡ Quick Start Guide
1. Set up virtual environment and install requirements
2. Run `setup_nltk.py` to download required NLTK data
3. Verify setup with `test_setup.py`
4. Run `main.py` to start the chatbot
5. Type 'quit' to exit the program

## 👥 Author
- Kasun Duara

---
💡 For any issues or questions, please open an issue in the repository.
