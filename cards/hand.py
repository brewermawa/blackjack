from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("card must be an instance of Card")
        
        if card in self.cards:
            raise ValueError(f"card {card} already in hand. Cannot add duplicate")

        self.cards.append(card)

    def remove_last_card(self):
        if len(self.cards) == 0:
            raise ValueError("Cannot remove card, hand is empty")

        return self.cards.pop()
    
    def clear(self):
        self.cards.clear()

    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    
    @property
    def cards_in_hand(self):
        return self.__len__()