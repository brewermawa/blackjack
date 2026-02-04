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
        self._player_doubled = False

    def initial_deal(self):
        self.player_hand.add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])
        self.player_hand.add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])

    def _blackjack(self):
        bj_dealer = BlackJackEval.blackjack(self.dealer_hand)
        bj_player = BlackJackEval.blackjack(self.player_hand)

        if bj_player and bj_dealer:
            return RoundOutcome.PUSH
        
        if bj_player and not bj_dealer:
            return RoundOutcome.BLACKJACK
        
        if not bj_player and bj_dealer:
            return RoundOutcome.LOSS
        
        return None

    def _surrender(self) -> bool:
        return BlackJackStrategy.strategy(self.player_hand, self.dealer_hand.cards[0]) == BlackJackStrategy.Action.SURRENDER

    def _player_turn(self):
        while True:
            action = BlackJackStrategy.strategy(self.player_hand, self.dealer_hand.cards[0])
            
            if action == BlackJackStrategy.Action.HIT:
                self.player_hand.add_card(self.deck.draw()[0])
                if BlackJackEval.bust(self.player_hand):
                    break
                continue
            elif action == BlackJackStrategy.Action.DOUBLE:
                self._player_doubled = True
                self.player_hand.add_card(self.deck.draw()[0])
                break
            elif action == BlackJackStrategy.Action.STAND:
                break
            else:
                raise NotImplementedError("SPLIT Not supported in v1.0")
            

    def _dealer_turn(self):
        while (
            BlackJackEval.value(self.dealer_hand) < 17 or
            (
                BlackJackEval.value(self.dealer_hand) == 17 and
                BlackJackEval.soft(self.dealer_hand) and self.hits_soft_17
            )
        ):
            self.dealer_hand.add_card(self.deck.draw()[0])
            if BlackJackEval.bust(self.dealer_hand):
                break


    def _compare(self):
        if BlackJackEval.bust(self.player_hand):
            if self._player_doubled:
                return RoundOutcome.DOUBLE_LOSS
            else:
                return RoundOutcome.LOSS
            
        if BlackJackEval.bust(self.dealer_hand):
            if self._player_doubled:
                return RoundOutcome.DOUBLE_WIN
            else:
                return RoundOutcome.WIN
            
        
        player_value = BlackJackEval.value(self.player_hand)
        dealer_value = BlackJackEval.value(self.dealer_hand)

        if player_value == dealer_value:
            return RoundOutcome.PUSH
        
        if player_value > dealer_value:
            if self._player_doubled:
                return RoundOutcome.DOUBLE_WIN
            else:
                return RoundOutcome.WIN
            
        if player_value < dealer_value:
            if self._player_doubled:
                return RoundOutcome.DOUBLE_LOSS
            else:
                return RoundOutcome.LOSS
            
        raise ValueError()

    def play(self):
        self.initial_deal()
        
        bj_result = self._blackjack()
        if bj_result is not None:
            return [bj_result]
        
        if self._surrender():
            return [RoundOutcome.HALF_PAY]

        self._player_turn()
        
        if not BlackJackEval.bust(self.player_hand):
            self._dealer_turn()

        return [self._compare()]

        



if __name__ == "__main__":
    deck = FixedDeck()
    deck.deck_for_player_bust()
    bj_round = BlackJackRound(deck=deck, hits_soft_17=True)
    print(bj_round.play())
    print("---", len(bj_round.dealer_hand))


    
        
 