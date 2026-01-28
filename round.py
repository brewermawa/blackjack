from cards.card import Card
from cards.deck import Deck
from fixed_deck import FixedDeck
from cards.hand import Hand
from roundoutcome import RoundOutcome
from strategy import BlackJackStrategy
from blackjack_eval import BlackJackEval

class BlackJackRound:
    def __init__(self, deck: Deck, hits_soft_17: bool) -> None:
        if not isinstance(deck, Deck):
            raise ValueError("deck must be an instance of Deck")
        
        if deck.jokers:
            raise ValueError("deck cannot contain jokers")
        
        if not isinstance(hits_soft_17, bool):
            raise ValueError("hits_soft_17 must be instance of bool")
        
        self.deck = deck
        self.hits_soft_17 = hits_soft_17
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def initial_deal(self):
        self.player_hand.add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])
        self.player_hand.add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])

    def _blackjack(self) -> bool:
        pass

    def _surrender(self) -> bool:
        return BlackJackStrategy.strategy(self.player_hand, self.dealer_hand.cards[0]) == BlackJackStrategy.Action.SURRENDER
            

    def _player_turn(self):
        pass

    def _dealer_turn(self):
        pass

    def _compare(self):
        pass

    def play(self):
        self.initial_deal()
        print(f"Player: {self.player_hand}")
        print(f"Dealer: {self.dealer_hand}")

        if self._surrender():
            return [RoundOutcome.HALF_PAY]
        
        if self._blackjack():
            return [RoundOutcome.BLACKJACK]

        self._player_turn()
        self._dealer_turn()
        self._compare()

        return None


if __name__ == "__main__":
    deck = FixedDeck()
    deck.deck_for_surrender()
    bj_round = BlackJackRound(deck=deck, hits_soft_17=False)
    print(bj_round.play())


    
        
