import random
from difflib import SequenceMatcher

class UserDatabase:
    """Manages user data storage and authentication."""

    def __init__(self):
        self.users = {
            "ploy_user": Member("U001", "Foodie", "1995-06-15", "Female", "Bangkok", ["SCB", "Krungsri"], "ploy_user", "Ploy", "ploy@example.com", "0123456789", "password123"),
            "john_doe": Member("U002", "Traveler", "1990-05-20", "Male", "Chiang Mai", ["Krungsri"], "john_doe", "John Doe", "john@example.com", "0987654321", "securepass")
        }

    def verify_user(self, username):
        """Checks if a user exists and returns the user object."""
        if username in self.users:
            print("\nUser found! Logging in...\n")
            return self.users[username]
        print("\nUser not found. Please register first.")
        return None


class Member:
    """Represents a user with personal details."""

    def __init__(self, user_id, lifestyle, dob, gender, location, cards, username, name, email, phone, password):
        self.user_id = user_id
        self.lifestyle = lifestyle
        self.dob = dob
        self.gender = gender
        self.location = location
        self.cards = cards
        self.username = username
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password


class RestaurantSelector:
    """Handles restaurant selection process, including recommendations."""

    def __init__(self):
        self.all_restaurants = [
            "MK Suki", "Shabu Indy", "Shabushi", "Shabu Kai Yang", "The Pizza Company",
            "After You", "Starbucks", "Suki Teenoi", "Suki Jinda", "Shabu House"
        ]

    def recommend_restaurants(self):
        """Displays only the top 5 recommended restaurants."""
        print("\nRecommended Restaurants:")
        for idx, restaurant in enumerate(self.all_restaurants[:5], start=1):
            print(f"{idx}. {restaurant}")

    def get_similarity(self, a, b):
        """Returns similarity percentage between two strings."""
        return SequenceMatcher(None, a.lower(), b.lower()).ratio() * 100

    def suggest_similar_restaurants(self, input_name):
        """Suggests up to 5 most similar restaurant names with match > 60%."""
        matches = [(restaurant, self.get_similarity(input_name, restaurant))
                   for restaurant in self.all_restaurants]

        # Filter matches > 60% and sort by highest match
        matches = sorted([m for m in matches if m[1] >= 60], key=lambda x: x[1], reverse=True)

        # Return only the top 5 matches
        return matches[:5]

    def select_restaurant(self):
        """Allows user to select restaurants until they type 'no'."""
        while True:
            print("\n--- Restaurant Selection ---")
            restaurant_name = input("Enter the restaurant name (or select by number, type 'no' to stop): ").strip()

            if restaurant_name.lower() == "no":
                break  # Exit the loop if the user types 'no'

            # Check if user selected a number
            if restaurant_name.isdigit():
                selection = int(restaurant_name)
                if 1 <= selection <= len(self.all_restaurants[:5]):
                    restaurant_name = self.all_restaurants[selection - 1]
                else:
                    print("Invalid selection. Please choose a valid restaurant.")
                    continue

            # If restaurant is not in the recommended list, suggest similar names
            if restaurant_name not in self.all_restaurants:
                suggestions = self.suggest_similar_restaurants(restaurant_name)
                if suggestions:
                    print("\nDid you mean one of these?")
                    for suggestion, match_percent in suggestions:
                        print(f"   - {suggestion} ({match_percent:.1f}% match)")
                    yield from suggestions  # Automatically recommend a card per restaurant
                else:
                    print("\nNo similar restaurants found.")
                continue  # Ask the user again

            print(f"\nYou selected: {restaurant_name}")
            yield restaurant_name  # Yield the selected restaurant so the caller can process it


class CardRecommender:
    """Handles card recommendations based on user lifestyle and benefits."""

    def __init__(self):
        self.cards = [
            Card("C001", "Platinum Rewards", "SCB", 5, 2, 15, "Free airport lounge access"),
            Card("C002", "Cashback Plus", "Krungsri", 7, 1, 10, "Travel insurance up to 5M THB"),
            Card("C003", "Dining Exclusive", "KBank", 3, 3, 20, "Priority restaurant reservations"),
            Card("C004", "Travel Pro", "Bangkok Bank", 2, 4, 5, "Bonus miles for flights"),
            Card("C005", "Shopping Master", "TMB", 4, 5, 12, "Extra discounts on e-commerce")
        ]

    def recommend_cards(self, restaurant_name):
        """Assigns 1 random credit card per restaurant selection."""
        card = random.choice(self.cards)
        print(f"\n💳 Recommended Credit Card for {restaurant_name}:")
        print(f"   - {card.card_name} ({card.bank})")
        print(f"   - Cashback: {card.cashback}%")
        print(f"   - Rewards: {card.rewards} points per 100 THB")
        print(f"   - Dining Discount: {card.dining_discount}% at selected restaurants")
        print(f"   - Travel Benefits: {card.travel_benefit}")


class Card:
    """Represents a credit card and its benefits."""

    def __init__(self, card_id, card_name, bank, cashback, rewards, dining_discount, travel_benefit):
        self.card_id = card_id
        self.card_name = card_name
        self.bank = bank
        self.cashback = cashback
        self.rewards = rewards
        self.dining_discount = dining_discount
        self.travel_benefit = travel_benefit


class PromotionFinderApp:
    """Main application class handling user authentication and restaurant selection."""

    def __init__(self):
        self.user_db = UserDatabase()
        self.restaurant_selector = RestaurantSelector()
        self.card_recommender = CardRecommender()

    def run(self):
        """Main application logic for user verification and restaurant selection."""
        print("Welcome to the Promotion Finder App!")

        # User authentication
        username = input("\nEnter your username: ").strip()
        user = self.user_db.verify_user(username)
        if not user:
            return  # Stop execution if user is not found

        self.restaurant_selector.recommend_restaurants()

        for restaurant in self.restaurant_selector.select_restaurant():
            self.card_recommender.recommend_cards(restaurant)

        print("\nThank you for using the app!")


# Run the application
if __name__ == "__main__":
    app = PromotionFinderApp()
    app.run()
