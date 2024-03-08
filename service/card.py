class Card:
    """
    This class represents a playing card.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self):
        """
        Return the value of the card as an integer.
        Returns:
            int: The value of the card.
        """
        if self.value in ["J", "Q", "K"]:
            return 10
        if self.value == "A":
            return 11
        return int(self.value)
