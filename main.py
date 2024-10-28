from travel_bot import TravelBot


def main():
    bot = TravelBot()
    print("Travel Booking Assistant (type 'quit' to exit)")
    print("=" * 50)

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break

        response = bot.process_input(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    main()
