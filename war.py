import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.rank_value(rank) # Assign the numeric value based on rank

    @staticmethod
    def rank_value(rank):
        """Map the rank to its corresponding numeric value."""
        values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        return values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        random.shuffle(self.cards) # Shuffle the deck

    @staticmethod
    def generate_deck():
        """Generate a standard deck of 52 cards."""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        return [Card(suit, rank) for suit in suits for rank in ranks]

def display_status(rounds_played, player1, player2):
    """Display the current status of the game."""
    print(f"Round {rounds_played}: Player 1 has {len(player1)} cards and Player 2 has {len(player2)} cards")
    input("Press enter to continue...")


# Play a single round of the game, comparing the cards and determining the winner of the round.
def play_round(player1, player2):
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    print(f"Player one has a {card1} Player two has a {card2}")
    if card1.value > card2.value:
        print("Player 1 won this round")
        player1 += [card1, card2]
    elif card1.value < card2.value:
        print("Player 2 won this round")
        player2 += [card1, card2]
    else: # handle war
        player1, player2 = handle_war(player1, player2, card1, card2)
    return player1, player2


# Handle the 'war' scenario, where players have cards of the same rank.
def handle_war(player1, player2, card1, card2):
    print("War!")
    # Additional logic for handling the "war" scenario
    # Collect cards in a temporary "pot"
    pot = [card1, card2]
    while card1.value == card2.value:
        if len(player1) < 4 or len(player2) < 4:
            # Not enough cards to continue the war game ends
            return player1, player2
        pot += [player1.pop(0) for _ in range(3)] + [player2.pop(0) for _ in range(3)]
        card1, card2 = player1.pop(0), player2.pop(0)
        pot += [card1, card2]

    # Determine winner of the war and give them the pot
    if card1.value > card2.value:
        player1 += pot
    else:
        player2 += pot

    return player1, player2


# Main game loop that handles the entire game play.
def game():
    deck = Deck()
    half = len(deck.cards) // 2
    player1 = deck.cards[:half]
    player2 = deck.cards[half:]
    rounds_played = 0

    while len(player1) > 0 and len(player2) > 0 and rounds_played < 50:
        rounds_played += 1
        display_status(rounds_played, player1, player2)
        player1, player2 = play_round(player1, player2)

    return determine_winner(player1, player2)


# Determine the winner based on the number of cards remaining.
def determine_winner(player1, player2):
    if len(player1) == len(player2):
        return "It's a tie!"
    elif len(player1) > len(player2):
        return "Player 1 is the winner!"
    else:
        return "Player 2 is the winner!"


# Entry point of the program.
def main():
    print("Are you ready for the war game? If yes press enter to continue...")
    input() # Wait for user to press enter
    winner = game()
    print(winner)

#TEST

if __name__ == "__main__":
    main()
