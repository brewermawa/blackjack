from cards.deck import Deck
from cards.hand import Hand
from blackjack.fixed_deck import FixedDeck
from blackjack.blackjack_eval import BlackJackEval
from blackjack.roundoutcome import RoundOutcome
from blackjack.strategy import BlackJackStrategy

class BlackJackRound:
    def __init__(self, deck: Deck, hits_soft_17: bool) -> None:
        if not isinstance(deck, Deck):
            raise TypeError("deck must be an instance of Deck")
        
        if deck.jokers:
            raise ValueError("deck cannot contain jokers")
        
        if not isinstance(hits_soft_17, bool):
            raise ValueError("hits_soft_17 must be instance of bool")
        
        self.deck = deck
        self.hits_soft_17 = hits_soft_17
        self.player_hands = [{"hand": Hand(), "doubled": False}]
        self.dealer_hand = Hand()
        self._player_doubled = []
        self._player_split = False


    def _initial_deal(self):
        self.player_hands[0]["hand"].add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])
        self.player_hands[0]["hand"].add_card(self.deck.draw()[0])
        self.dealer_hand.add_card(self.deck.draw()[0])


    def _blackjack(self):
        bj_dealer = BlackJackEval.blackjack(self.dealer_hand)
        bj_player = BlackJackEval.blackjack(self.player_hands[0]["hand"])

        if bj_player and bj_dealer:
            return RoundOutcome.PUSH
        
        if bj_player and not bj_dealer:
            return RoundOutcome.BLACKJACK
        
        if not bj_player and bj_dealer:
            return RoundOutcome.LOSS
        
        return None


    def _surrender(self) -> bool:
        return BlackJackStrategy.strategy(self.player_hands[0]["hand"], self.dealer_hand.cards[0]) == BlackJackStrategy.Action.SURRENDER


    def _split(self):
        """
        1. check strategy to see if correct move is split (return None if not split)
        2. (it is split) append new hand to player_hands
        3. remove card from player_hands[0] and add it to player_hands[1]
        """
        if BlackJackStrategy.strategy(self.player_hands[0]["hand"], self.dealer_hand.cards[0]) == BlackJackStrategy.Action.SPLIT:
            self.player_hands.append({"hand": Hand(), "doubled": False})
            self.player_hands[1]["hand"].add_card(self.player_hands[0]["hand"].remove_last_card())
            self._player_split = True

  
    def _player_turn(self):
        for player_hand in self.player_hands:
            if len(player_hand["hand"].cards) == 1:
                player_hand["hand"].add_card(self.deck.draw()[0])

            while BlackJackEval.value(player_hand["hand"]) < 21:
                if len(player_hand["hand"].cards) == 2 and BlackJackEval.blackjack(player_hand["hand"]):
                    break
                if self._player_split and player_hand["hand"].cards[0].rank == "A":
                    break
                action = BlackJackStrategy.strategy(player_hand["hand"], self.dealer_hand.cards[0])

                if action == BlackJackStrategy.Action.SURRENDER:
                    #In this situation, SURRENDER happened if the player has more than two cards or there was a split.
                    #Since SURRENDER is not valid with wither more than 2 cards or after a split, it should be a hit
                    player_hand["hand"].add_card(self.deck.draw()[0])
                    
                    if BlackJackEval.bust(player_hand["hand"]):
                        break
                    continue
                
                if action == BlackJackStrategy.Action.HIT:
                    player_hand["hand"].add_card(self.deck.draw()[0])
                    
                    if BlackJackEval.bust(player_hand["hand"]):
                        break
                    continue
                elif action == BlackJackStrategy.Action.DOUBLE:
                    player_hand["doubled"] = True
                    player_hand["hand"].add_card(self.deck.draw()[0])
                    break
                
                elif action == BlackJackStrategy.Action.SPLIT and self._player_split:
                    #raise NotImplementedError("Only one split in v2.0")
                    if BlackJackEval.value(player_hand["hand"]) <= 10:
                        player_hand["hand"].add_card(self.deck.draw()[0])
                    break

                
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
        hand = player_hand["hand"]
        doubled = player_hand["doubled"]

        if BlackJackEval.bust(hand):
            if doubled:
                return RoundOutcome.DOUBLE_LOSS
            else:
                return RoundOutcome.LOSS
            
        if BlackJackEval.bust(self.dealer_hand):
            if doubled:
                return RoundOutcome.DOUBLE_WIN
            else:
                return RoundOutcome.WIN
            
        player_value = BlackJackEval.value(hand)
        dealer_value = BlackJackEval.value(self.dealer_hand)

        if player_value == dealer_value:
            return RoundOutcome.PUSH
        
        if player_value > dealer_value:
            if doubled:
                return RoundOutcome.DOUBLE_WIN
            else:
                return RoundOutcome.WIN
            
        if player_value < dealer_value:
            if doubled:
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
        bust = all([BlackJackEval.bust(player_hand["hand"]) for player_hand in self.player_hands])
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
    #deck.deck_for_split_no_surrender()
    #deck.deck_for_double_loss()
    deck.deck_for_surrender_to_hit_when_more_than_2_cards()
    bj_round = BlackJackRound(deck=deck, hits_soft_17=True)
    #bj_round.play()
    print(bj_round.play())
    #print("---", len(bj_round.dealer_hand))
