import random
from service.card import Card

class Deck:
    """
    This is a class representing a deck of cards.
    This class initializes a full deck of 52 cards and provides methods for
    shuffling the deck, drawing cards, and building a fresh deck from scratch.
    """
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """
        Build a full deck of 52 cards.
        This method initializes a full deck of 52 cards, with one card for each
        combination of suit and value.
        """
        for suit in ["HEART", "DIAMOND", "CLUB", "SPADE"]:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        """
        Shuffle the deck of cards.
        This method shuffles the deck of cards in-place, using the Fisher-Yates
        shuffle algorithm.
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        Draw and return the top card from the deck.
        This method draws the top card from the deck and returns it,
        removing it from the deck in the process.
        """
        return self.cards.pop()
