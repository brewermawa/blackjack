from fixed_deck import FixedDeck
from cards.deck import Deck
from cards.hand import Hand
from blackjack_eval import BlackJackEval
from roundoutcome import RoundOutcome
from strategy import BlackJackStrategy

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
        self.player_hands = [Hand()]
        self.dealer_hand = Hand()
        self._player_doubled = False
        self._player_split = False


    def _initial_deal(self):
        self.player_hands[0].add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])
        self.player_hands[0].add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])


    def _blackjack(self):
        bj_dealer = BlackJackEval.blackjack(self.dealer_hand)
        bj_player = BlackJackEval.blackjack(self.player_hands[0])

        if bj_player and bj_dealer:
            return RoundOutcome.PUSH
        
        if bj_player and not bj_dealer:
            return RoundOutcome.BLACKJACK
        
        if not bj_player and bj_dealer:
            return RoundOutcome.LOSS
        
        return None


    def _surrender(self) -> bool:
        return BlackJackStrategy.strategy(self.player_hands[0], self.dealer_hand.cards[0]) == BlackJackStrategy.Action.SURRENDER


    def _split(self):
        """
        1. check strategy to see if correct move is split (return None if not split)
        2. (it is split) append new hand to player_hands
        3. remove card from player_hands[0] and add it to player_hands[1]
        """

        if BlackJackStrategy.strategy(self.player_hands[0], self.dealer_hand.cards[0]) == BlackJackStrategy.Action.SPLIT:
            self.player_hands.append(Hand())
            self.player_hands[1].add_card(self.player_hands[0].remove_last_card())
            self._player_split = True

    
    def _player_turn(self):
        for player_hand in self.player_hands:
            if len(player_hand.cards) == 1:
                player_hand.add_card(self.deck.draw()[0])

            while True:
                if len(player_hand.cards) == 2 and BlackJackEval.blackjack(player_hand):
                    break
                if self._player_split and player_hand.cards[0].rank == "A":
                    break
                action = BlackJackStrategy.strategy(player_hand, self.dealer_hand.cards[0])
                
                if action == BlackJackStrategy.Action.HIT:
                    player_hand.add_card(self.deck.draw()[0])
                    
                    if BlackJackEval.bust(player_hand):
                        break
                    continue
                elif action == BlackJackStrategy.Action.DOUBLE:
                    if self._player_split:
                        raise NotImplementedError("DAS Not supported in v2.0")
                    self._player_doubled = True
                    player_hand.add_card(self.deck.draw()[0])
                    break
                elif action == BlackJackStrategy.Action.SURRENDER and self._player_split:
                    raise NotImplementedError("SURRENDER Not valid after split in v2.0")
                elif action == BlackJackStrategy.Action.SPLIT and self._player_split:
                    raise NotImplementedError("Only one split in v2.0")
                elif action == BlackJackStrategy.Action.STAND:
                    break


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


    def _compare(self, player_hand):
        if BlackJackEval.bust(player_hand):
            if self._player_doubled:
                return RoundOutcome.DOUBLE_LOSS
            else:
                return RoundOutcome.LOSS
            
        if BlackJackEval.bust(self.dealer_hand):
            if self._player_doubled:
                return RoundOutcome.DOUBLE_WIN
            else:
                return RoundOutcome.WIN
            
        player_value = BlackJackEval.value(player_hand)
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
        #1. Deal initial cards: player, dealer, player, dealer
        self._initial_deal()

        #2. blackjack check (possible play() termination)
        bj_result = self._blackjack()
        if bj_result is not None:
            return [bj_result]
        
        #3. surrender check (possible play() termination)
        if self._surrender():
            return [RoundOutcome.HALF_PAY]
        
        #4. split check
        self._split()

        #5. player turn
        self._player_turn()

        #6. dealer turn (only if at least one player hand is not bust)
        bust = all([BlackJackEval.bust(player_hand) for player_hand in self.player_hands])
        if not bust:
            self._dealer_turn()

        #7. compare hands
        outcomes = []
        for player_hand in self.player_hands:
            outcomes.append(self._compare(player_hand))

        return outcomes






if __name__ == "__main__":
    deck = FixedDeck()
    #deck.deck_for_bj()
    #deck.deck_for_split_AA_win_win()
    #deck.deck_for_split_AA_then_KK_dealer_21()
    #deck.deck_for_split_AA_only_one_extra_card_per_hand()
    #deck.deck_for_split_win_one_loss_one()
    deck.deck_for_split_then_surrender()
    bj_round = BlackJackRound(deck=deck, hits_soft_17=True)
    #bj_round.play()
    print(bj_round.play())
    #print("---", len(bj_round.dealer_hand))
