from cards.deck import Deck
from cards.hand import Hand


class BlackJackRound:
    def __init__(self, deck: Deck, hits_soft_17: bool) -> None:
        if not isinstance(deck, Deck):
            raise TypeError("deck must be an instance of Deck")
        
        if deck.jokers:
            raise ValueError("deck cannot contain jokers")
        
        if not isinstance(hits_soft_17, bool):
            raise TypeError("hits_soft_17 must be instance of bool")
        
        self.deck = deck
        self.hits_soft_17 = hits_soft_17
        self.player_hands = [{"hand": Hand(), "doubled": False, "surrendered": False}]
        self.dealer_hand = Hand()
