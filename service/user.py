import json
from typing import Optional

class User:
    """
    This class represents a user in a game.
    """

    def __init__(self, name: str, chips: int = 1000):
        self.name = name
        self.chips = chips
        self.highest_amount = chips

    def bet(self, amount: int):
        """
        Place a bet with a specified number of chips.
        Args:
            amount (int): The number of chips to bet.
        Returns:
            bool: True if the bet was successful, False otherwise.
        """
        if amount <= self.chips:
            self.chips -= amount
            return True
        return False

    def win(self, amount: int):
        """
        Add chips to the user's total.
        Args:
            amount (int): The number of chips to add.
        """
        self.chips += amount
        if self.chips > self.highest_amount:
            self.highest_amount = self.chips

    def save(self):
        """
        Save the user's data to a JSON file.
        """
        with open("./data/users.json", "r+") as file:
            users = json.load(file)
            users[self.name] = {
                "chips": self.chips,
                "highest_amount": self.highest_amount
            }
            file.seek(0)
            json.dump(users, file)

    @classmethod
    def load(cls, name: str) -> Optional['User']:
        """
        Load a user's data from a JSON file and return a new user object.
        Args:
            name (str): The user's name.
        Returns:
            Optional[User]: A new user object with the user's data, or None if the
                user does not exist in the JSON file.
        """
        with open("./data/users.json", "r") as file:
            users = json.load(file)
            if name in users:
                user_data = users[name]
                user = User(name, user_data["chips"])
                user.highest_amount = user_data["highest_amount"]
                return user
        return None
