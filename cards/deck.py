import random
from math import ceil

from card import Card

class Deck:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♠", "♥"]
    JOKERS = [("Joker", "🃏"), ("Joker", "🃏")]
    
    def __init__(self, number_of_decks: int=1, jokers: bool=False):
        if not isinstance(number_of_decks, int) or isinstance(number_of_decks, bool):
            raise TypeError("Number of decks must be an integer")
        
        if number_of_decks < 1:
            raise ValueError("Number of decks must be greater to or equal to 1")

        self.decks = number_of_decks
        self.jokers = jokers
        self._deck = []
        self._cut_point = None
        self._len_full_deck = (52 * self.decks) + (2 * self.decks * self.jokers)
        self.needs_shuffle = False

        self.shuffle()

    def _build_deck(self):
        self._deck = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]

        if self.jokers:
            for joker in self.JOKERS:
                self._deck.append(Card(joker[0], joker[1]))

        self._deck = self._deck * self.decks

    def set_cut_point(self, percent=None):
        if len(self._deck) != self._len_full_deck:
            raise ValueError("cut point can only be set on a full deck")
        
        if self._cut_point:
            raise ValueError("cut point already set, cannot set it a second time")
        
        if percent is not None:
            if percent < 0.7 or percent > 0.8:
                raise ValueError("percent must be between 0.7 and 0.8 inclusive")
        else:
            percent = random.randint(70, 80) / 100

        self._cut_point = self._len_full_deck - self._len_full_deck * percent


    def shuffle(self):
        self._build_deck()
        self.needs_shuffle = False
        self._cut_point = None
        random.shuffle(self._deck)

    def draw(self, cards=1):
        if not isinstance(cards, int) or isinstance(cards, bool):
            raise TypeError("Cards to draw must be an integer")
        
        if cards < 1:
            raise ValueError("Cards to draw must be greater to or equal to 1")
        
        return_cards = []

        if cards > len(self._deck):
            raise IndexError(f"{len(self._deck)} cards left in the deck. Cannot draw {cards}")

        for _ in range(cards):
            return_cards.append(self._deck.pop())

        if self._cut_point:
            if len(self._deck) <= self._cut_point:
                self.needs_shuffle = True

        return return_cards
    
    def burn(self):
        if len(self._deck) == 0:
            raise IndexError("No cards left in deck, cannot burn card")
        
        self._deck.pop()

        return True

    @property
    def cards_remaining(self):
        return self.__len__()

    def __len__(self):
        return len(self._deck)

    def __str__(self):
        return f"Deck with {len(self._deck)} remaining cards."


if __name__ == "__main__":
    deck = Deck(1, True)
    print(deck)