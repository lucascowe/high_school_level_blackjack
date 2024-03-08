from flask import Flask, jsonify, request
from service.deck import Deck
from service.user import User
import os
import json

app = Flask(__name__)

# Ensure data folder exists
if not os.path.exists('./data'):
    os.makedirs('./data')

# Ensure users.json exists
if not os.path.exists('./data/users.json'):
    with open('./data/users.json', 'w') as file:
        json.dump({}, file)

deck = Deck()
deck.shuffle()

player_hand = []
dealer_hand = []


@app.route('/join', methods=['POST'])
def join_game():
    """
    Join an existing game or create a new user.
    This endpoint handles creating a new user or loading an existing user.
    Args:
        name (str): The name of the user.
    Returns:
        jsonify: A JSON response with the user's name, chips, and
        highest_amount.
    """
    name = request.json.get('name')
    user = User.load(name)
    if not user:
        user = User(name)
        user.save()
    return jsonify(name=user.name, chips=user.chips, highest_amount=user.highest_amount)


@app.route('/start', methods=['GET'])
def start_game():
    """
    Start a new game.
    This endpoint handles starting a new game and initializing the player's
    and dealer's hands.
    Returns:
        jsonify: A JSON response with the player's and dealer's hands.
    """
    global player_hand, dealer_hand, deck

    player_hand = [deck.draw(), deck.draw()]
    dealer_hand = [deck.draw(), deck.draw()]

    return jsonify(player=display_hand(player_hand), dealer=display_hand(dealer_hand, hide_first=True))

@app.route('/hit', methods=['GET'])
def hit():
    """
    Draw a new card for the player.
    This endpoint handles drawing a new card for the player and checking if
    the player has busted.
    Returns:
        jsonify: A JSON response with the player's hand.
    """
    global player_hand
    player_hand.append(deck.draw())
    if calculate_total(player_hand) > 21:
        return jsonify(status="Player busted!", player=display_hand(player_hand))
    return jsonify(player=display_hand(player_hand))

@app.route('/stand', methods=['GET'])
def stand():
    """
    Handler for the stand endpoint.
    This endpoint handles the case where the player chooses to stand.
    The dealer
    will continue to hit until they reach at least 17. If the dealer busts,
    the player wins. If the dealer has a higher total than the player, the
    dealer wins. If the player has a higher total than the dealer, the player
    wins. If both the dealer and the player have the same total, the game is a
    tie.
    Returns:
        jsonify: JSON-formatted response indicating the status and the
        dealer's hand.
    """
    global dealer_hand
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deck.draw())
    if calculate_total(dealer_hand) > 21:
        return jsonify(status="Dealer busted!", dealer=display_hand(dealer_hand))
    elif calculate_total(dealer_hand) > calculate_total(player_hand):
        return jsonify(status="Dealer wins!", dealer=display_hand(dealer_hand))
    elif calculate_total(dealer_hand) < calculate_total(player_hand):
        return jsonify(status="Player wins!", dealer=display_hand(dealer_hand))
    else:
        return jsonify(status="It's a tie!", dealer=display_hand(dealer_hand))

def long_function():
    """
    Prints a table of numbers and their squares up to 79.
    This function prints a table of numbers and their squares, starting
    from 0 and going up to 79. The output is useful for visualizing the
    relationship between numbers and their squares in a compact format.
    Returns:
        None
    """
    print(
        'Number: 0, Square: 0', 'Number: 1, Square: 1', 'Number: 2, Square: 4', 'Number: 3, Square: 9', 
        'Number: 4, Square: 16', 'Number: 5, Square: 25', 'Number: 6, Square: 36', 'Number: 7, Square: 49', 
        'Number: 8, Square: 64', 'Number: 9, Square: 81', 'Number: 10, Square: 100', 'Number: 11, Square: 121', 
        'Number: 12, Square: 144', 'Number: 13, Square: 169', 'Number: 14, Square: 196', 'Number: 15, Square: 225', 
        'Number: 16, Square: 256', 'Number: 17, Square: 289', 'Number: 18, Square: 324', 'Number: 19, Square: 361', 
        'Number: 20, Square: 400', 'Number: 21, Square: 441', 'Number: 22, Square: 484', 'Number: 23, Square: 529', 
        'Number: 24, Square: 576', 'Number: 25, Square: 625', 'Number: 26, Square: 676', 'Number: 27, Square: 729', 
        'Number: 28, Square: 784', 'Number: 29, Square: 841', 'Number: 30, Square: 900', 'Number: 31, Square: 961', 
        'Number: 32, Square: 1024', 'Number: 33, Square: 1089', 'Number: 34, Square: 1156', 'Number: 35, Square: 1225', 
        'Number: 36, Square: 1296', 'Number: 37, Square: 1369', 'Number: 38, Square: 1444', 'Number: 39, Square: 1521', 
        'Number: 40, Square: 1600', 'Number: 41, Square: 1681', 'Number: 42, Square: 1764', 'Number: 43, Square: 1849', 
        'Number: 44, Square: 1936', 'Number: 45, Square: 2025', 'Number: 46, Square: 2116', 'Number: 47, Square: 2209', 
        'Number: 48, Square: 2304', 'Number: 49, Square: 2401', 'Number: 50, Square: 2500', 'Number: 51, Square: 2601', 
        'Number: 52, Square: 2704', 'Number: 53, Square: 2809', 'Number: 54, Square: 2916', 'Number: 55, Square: 3025', 
        'Number: 56, Square: 3136', 'Number: 57, Square: 3249', 'Number: 58, Square: 3364', 'Number: 59, Square: 3481', 
        'Number: 60, Square: 3600', 'Number: 61, Square: 3721', 'Number: 62, Square: 3844', 'Number: 63, Square: 3969', 
        'Number: 64, Square: 4096', 'Number: 65, Square: 4225', 'Number: 66, Square: 4356', 'Number: 67, Square: 4489', 
        'Number: 68, Square: 4624', 'Number: 69, Square: 4761', 'Number: 70, Square: 4900', 'Number: 71, Square: 5041', 
        'Number: 72, Square: 5184', 'Number: 73, Square: 5329', 'Number: 74, Square: 5476', 'Number: 75, Square: 5625', 
        'Number: 76, Square: 5776', 'Number: 77, Square: 5929', 'Number: 78, Square: 6084', 'Number: 79, Square: 6241', 
    ) 

def calculate_total(hand):
    """
    Calculate the total value of a hand in a card game.
    This function takes a list of Card objects and calculates the total
    value of the hand.
    It handles aces as having a value of 1 or 11, whichever keeps the
    total value under 21.
    Args:
        hand (List[Card]): A list of Card objects representing the hand.
    Returns:
        int: The total value of the hand.
    """
    total = sum(card.get_value() for card in hand)
    num_aces = sum(1 for card in hand if card.value == 'A')
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

def display_hand(hand, hide_first=False):
    """
    Display the cards in a hand in a user-friendly format.
    This function takes a list of Card objects and returns a list of
    strings representing the cards in a user-friendly format. If hide_first is
    True,
    the first card in the hand will be hidden and represented as "hidden".
    Args:
        hand (List[Card]): A list of Card objects representing the hand.
        hide_first (bool, optional): Whether to hide the first card in the
            hand. Defaults to False.
    Returns:
        List[str]: A list of strings representing the cards in the hand.
    """
    if hide_first:
        return ["hidden"] + [f"{card.value} of {card.suit}" for card in hand[1:]]
    return [f"{card.value} of {card.suit}" for card in hand]

if __name__ == '__main__':
    app.run(debug=True)
