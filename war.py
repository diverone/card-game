import random

# Card game "War" Setup:

# 1. Create the basic structures:

#    - Create a Card class: Each card has a suit and rank.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # Dictionary to map rank names to numeric values for comparison
        values = {
            "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9,
            "10": 10, "Jack": 11, "Queen": 12,
            "King": 13, "Ace": 14
        }
        # Assign the numeric value for the card based on its rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def compare_to(self, other_card):
        # Compare this card's value to another card's value
        if self.value > other_card.value:
            return self
        elif self.value < other_card.value:
            return other_card
        else:
            return None  # Tie
    

#    - Create a Deck class: The deck contains 52 cards, shuffled randomly.
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __str__(self):
        return f"{len(self.cards)} cards left in the deck."
    

#    - Create a Player class: Each player has a name and a hand of cards.
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        return self.hand.pop(0)

    def add_cards(self, cards):
        self.hand.extend(cards)

    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards."

# 2. Shuffling and Dealing:
#    - In the Deck class, implement methods to shuffle the cards and deal cards to players.
def main():
    #26 cards for each player
    deck = Deck()
    half = len(deck.cards) // 2
    player1 = deck.cards[:half]
    player2 = deck.cards[half:]   
    winner=game(player1, player2)
    print(winner) 



# 3. Game Logic:
#    - In the Player class, implement methods to draw a card from their hand and compare cards with another player.
#    - In the main game loop, players take turns drawing cards, comparing ranks, and resolving "war" scenarios.


# 4. Winning:
#    - Keep track of the number of cards each player has. The player with all the cards wins.


# 5. User Interaction:
#    - Display game prompts to the user for each round.
#    - Show the cards played by both players and the outcome of each round.
#    - Display the winner at the end of the game.


# 6. Error Handling:
#    - Handle cases where players run out of cards, especially during "war" scenarios.

# Create cards
card1 = Card("Hearts", "Ace")
card2 = Card("Clubs", "King")

print(card1)  # Output: Ace of Hearts
print(card2)  # Output: King of Clubs

# Create a deck and check its contents
deck = Deck()
print(deck)  # Output: 52 cards left in the deck

# Deal a card
dealt_card = deck.deal()
print(dealt_card)  # Output: Will show one of the cards, e.g., 2 of Hearts
print(deck)  # Output: 51 cards left in the deck

# Create players
player1 = Player("Alice")
player2 = Player("Bob")

# Add cards to players' hands
player1.add_cards([card1, card2])
player2.add_cards([dealt_card])

print(player1)  # Output: Alice has 2 cards.
print(player2)  # Output: Bob has 1 cards.

# Draw a card from player's hand
drawn_card = player1.draw()
print(drawn_card)  # Output: Ace of Hearts (since card1 was added first)
print(player1)  # Output: Alice has 1 cards.

# Create two cards with different values
card1 = Card("Hearts", "Ace")  # Value = 14
card2 = Card("Clubs", "King")  # Value = 13

# Compare them using the compare_to method
winner_card = card1.compare_to(card2)

# Print the result
if winner_card is card1:
    print("Card 1 wins!")  # Output: Card 1 wins!
elif winner_card is card2:
    print("Card 2 wins!") # Output: Card 2 wins!
else:
    print("It's a tie!")

# Create a deck and check its contents
deck = Deck()
print(deck)  # Output: 52 cards left in the deck

# Deal a card
dealt_card = deck.deal()
print(dealt_card)  # Output: Will show one of the cards, e.g., 2 of Hearts
print(deck)  # Output: 51 cards left in the deck
