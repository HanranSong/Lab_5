"""
There are four suits in this lab, each suits has 13 ranks. Each round the cards will be shuffled. Two players will take
five cards, the one have more Ace card will win the game. If they have same number of Ace card, they will restart the
game including reshuffle and redraw the card.
"""

import random


class Card:
    # Card class represent a card, including its rank and suit.
    def __init__(self, rank, suit):
        # Initialize a card with a given suit and a rank
        #   rank - an integer between 1-13
        #   suit- a string ("Clubs", "Diamonds", "Hearts", "Spades")
        self.rank = rank
        self.suit = suit
        self.rank_letter = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
                            'Queen', 'King')

    def get_rank(self):
        # Return the rank of a card
        return self.rank

    def display(self):
        # Display a card as a string with the name of the rank and the name of the suit (e.g. 'Jack of Diamonds',
        # 'Three of Clubs')
        return self.rank_letter[Card.get_rank(self) - 1] + ' of ' + self.suit


class Deck:
    # Deck class represent the table, there are 52 different cards in it.
    def __init__(self):
        # Initialize a deck by generating one of each possible card using the Card class. The deck should contain one
        # Card object for each of the 4*13=52 different cards.
        self.suit = ("Clubs", "Diamonds", "Hearts", "Spades")
        self.all_card = list()
        self.the_card = Card
        for s in self.suit:
            for r in range(0, 13):
                self.all_card.append(Card(r, s))

    def shuffle(self):
        # Randomly shuffle the deck of cards
        random.shuffle(self.all_card)

    def deal(self):
        # Return a card from the top of the deck, and remove that card from the deck.
        self.the_card = self.all_card[0]
        self.all_card.pop(0)
        return self.the_card


class Player:
    # Player class represent a player's action, include adding cards, counting Ace cards, and displaying cards.
    def __init__(self):
        # Initialize a player who can keep track of the cards in their hand. Initially, the hand should be empty (no
        # cards in it).
        self.cards_in_hand = list()
        self.num_ace = 0

    def add(self, card):
        # Add a card to the player’s hand
        #   card - An instance of the Card class.
        self.cards_in_hand.append(card)

    def ace_cards(self):
        # Returns the number of Ace cards in the player’s hand.
        for i in self.cards_in_hand:
            if i.get_rank() == 1:
                self.num_ace += 1
        return self.num_ace

    def display(self):
        # Display the player’s hand. This method should call the display() method of each card object in the player's
        # hand.
        for i in self.cards_in_hand:
            print(i.display())


def main():
    # Create one deck
    # Shuffle the deck
    # Create both players
    # Populate the player's hands with 5 cards each
    # Display the player's hands
    # Display the number of Ace cards in each player’s hand
    # Display the winner.
    # If the game ends in a tie, then restart the game from step a.
    key = True
    while key:
        deck = Deck()
        deck.shuffle()
        player_one = Player()
        player_two = Player()
        for i in range(5):
            player_one.add(deck.deal())
            player_two.add(deck.deal())
        print('This is the hand of player 1:')
        player_one.display()
        print('\nThis is the hand of player 2:')
        player_two.display()
        print('\nNumber of ace cards in each player\'s hand:')
        print('Player 1 has', player_one.ace_cards(), 'aces')
        print('Player 2 has', player_two.ace_cards(), 'aces')
        print('\nResult:')
        if player_one.ace_cards() > player_two.ace_cards():
            print('Player 1 is the winner')
            key = False
        elif player_one.ace_cards() < player_two.ace_cards():
            print('Player 2 is the winner')
            key = False
        else:
            print('No winner, shuffle again\n')


main()
