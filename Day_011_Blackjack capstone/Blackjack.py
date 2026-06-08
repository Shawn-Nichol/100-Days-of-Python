import random
from art import logo


def deal_cards():
    """Deals a random card from the deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)

def calculate_score(cards):
    """Counts the total value of the cards dealt"""
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0

    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total

def compare(player_score, dealer_score):
    """Compares the player score and the dealer score."""
    if player_score == dealer_score:
        return "draw"
    elif dealer_score == 0:
        return "lose, opponent has blackjack"
    elif player_score == 0:
        return "Win with a blackjack"
    elif player_score > 21:
        return "Bust, you lose"
    elif dealer_score > 21:
        return "Dealer busts, you win"
    elif player_score > dealer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    player_cards = []
    dealer_cards = []
    dealer_score = -1
    player_score = -1
    game_over = False

    for _ in range(2):
        player_cards.append(deal_cards())
        dealer_cards.append(deal_cards())


    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score >21:
            game_over = True
        else:
            deal_card = input("Hit or Stay?").title()
            if deal_card == "Hit":
                player_cards.append(deal_cards())
            else:
                game_over = True

    while dealer_score !=0 and dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards},final score: {dealer_score}")
    print(compare(player_score, dealer_score))

print(logo)
while input("Do you want to play a game of blackjack? Type 'y'  or 'n': ") == "y":
    play_game()
