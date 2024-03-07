class Card:
    """
    This class represents a playing card.
    """
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def get_value(self) -> int:
        if self.value in ["J", "Q", "K"]:
            return 10
        if self.value == "A":
            return 11
        return int(self.value)
