from enum import Enum

from cards.card import Card
from cards.hand import Hand
from blackjack_eval import BlackJackEval

class BlackJackStrategy:
    class Action(Enum):
        HIT = "hit"
        STAND = "stand"
        DOUBLE = "double"
        SPLIT = "split"
        SURRENDER = "surrender"

    H = Action.HIT
    S = Action.STAND
    D = Action.DOUBLE
    P = Action.SPLIT
    R = Action.SURRENDER

    HARD_STRATEGY: dict[int, dict[str, Action]] = {
        # 5–8: H H H H H H H H H H
        5:  {"2": H, "3": H, "4": H, "5": H, "6": H, "7": H, "8": H, "9": H, "10": H, "A": H},
        6:  {"2": H, "3": H, "4": H, "5": H, "6": H, "7": H, "8": H, "9": H, "10": H, "A": H},
        7:  {"2": H, "3": H, "4": H, "5": H, "6": H, "7": H, "8": H, "9": H, "10": H, "A": H},
        8:  {"2": H, "3": H, "4": H, "5": H, "6": H, "7": H, "8": H, "9": H, "10": H, "A": H},

        # 9: H D D D D H H H H H
        9:  {"2": H, "3": D, "4": D, "5": D, "6": D, "7": H, "8": H, "9": H, "10": H, "A": H},

        # 10: D D D D D D D D H H
        10: {"2": D, "3": D, "4": D, "5": D, "6": D, "7": D, "8": D, "9": D, "10": H, "A": H},

        # 11: D D D D D D D D D H
        11: {"2": D, "3": D, "4": D, "5": D, "6": D, "7": D, "8": D, "9": D, "10": D, "A": H},

        # 12: H H S S S H H H H H
        12: {"2": H, "3": H, "4": S, "5": S, "6": S, "7": H, "8": H, "9": H, "10": H, "A": H},

        # 13–14: S S S S S H H H H H
        13: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": H, "8": H, "9": H, "10": H, "A": H},
        14: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": H, "8": H, "9": H, "10": H, "A": H},

        # 15: S S S S S H H H R H
        15: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": H, "8": H, "9": H, "10": R, "A": H},

        # 16: S S S S S H H R R R
        16: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": H, "8": H, "9": R, "10": R, "A": R},

        # 17+: S S S S S S S S S S
        17: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": S, "8": S, "9": S, "10": S, "A": S},
        18: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": S, "8": S, "9": S, "10": S, "A": S},
        19: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": S, "8": S, "9": S, "10": S, "A": S},
        20: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": S, "8": S, "9": S, "10": S, "A": S},
        21: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": S, "8": S, "9": S, "10": S, "A": S},
    }

    SOFT_STRATEGY: dict[int, dict[str, Action]] = {
        # A,2 (13): H H H D D H H H H H
        13: {"2": H, "3": H, "4": H, "5": D, "6": D, "7": H, "8": H, "9": H, "10": H, "A": H},

        # A,3 (14): H H H D D H H H H H
        14: {"2": H, "3": H, "4": H, "5": D, "6": D, "7": H, "8": H, "9": H, "10": H, "A": H},

        # A,4 (15): H H D D D H H H H H
        15: {"2": H, "3": H, "4": D, "5": D, "6": D, "7": H, "8": H, "9": H, "10": H, "A": H},

        # A,5 (16): H H D D D H H H H H
        16: {"2": H, "3": H, "4": D, "5": D, "6": D, "7": H, "8": H, "9": H, "10": H, "A": H},

        # A,6 (17): H D D D D H H H H H
        17: {"2": H, "3": D, "4": D, "5": D, "6": D, "7": H, "8": H, "9": H, "10": H, "A": H},

        # A,7 (18): S D D D D S S H H H
        18: {"2": S, "3": D, "4": D, "5": D, "6": D, "7": S, "8": S, "9": H, "10": H, "A": H},

        # A,8 (19): S S S S D S S S S S
        19: {"2": S, "3": S, "4": S, "5": S, "6": D, "7": S, "8": S, "9": S, "10": S, "A": S},

        # A,9 (20): S S S S S S S S S S
        20: {"2": S, "3": S, "4": S, "5": S, "6": S, "7": S, "8": S, "9": S, "10": S, "A": S},
    }

    PAIR_STRATEGY: dict[str, dict[str, Action]] = {
        # A,A: P P P P P P P P P P
        "A":  {"2": P, "3": P, "4": P, "5": P, "6": P, "7": P, "8": P, "9": P, "10": P, "A": P},

        # 10,10: S S S S S S S S S S
        "10": {"2": S, "3": S, "4": S, "5": S, "6": S, "7": S, "8": S, "9": S, "10": S, "A": S},

        # 9,9: P P P P P S P P S S
        "9":  {"2": P, "3": P, "4": P, "5": P, "6": P, "7": S, "8": P, "9": P, "10": S, "A": S},

        # 8,8: P P P P P P P P P P
        "8":  {"2": P, "3": P, "4": P, "5": P, "6": P, "7": P, "8": P, "9": P, "10": P, "A": P},

        # 7,7: P P P P P P H H H H
        "7":  {"2": P, "3": P, "4": P, "5": P, "6": P, "7": P, "8": H, "9": H, "10": H, "A": H},

        # 6,6: P P P P P H H H H H
        "6":  {"2": P, "3": P, "4": P, "5": P, "6": P, "7": H, "8": H, "9": H, "10": H, "A": H},

        # 5,5: D D D D D D D D H H
        "5":  {"2": D, "3": D, "4": D, "5": D, "6": D, "7": D, "8": D, "9": D, "10": H, "A": H},

        # 4,4: H H H P P H H H H H
        "4":  {"2": H, "3": H, "4": H, "5": P, "6": P, "7": H, "8": H, "9": H, "10": H, "A": H},

        # 3,3: P P P P P P H H H H
        "3":  {"2": P, "3": P, "4": P, "5": P, "6": P, "7": P, "8": H, "9": H, "10": H, "A": H},

        # 2,2: P P P P P P H H H H
        "2":  {"2": P, "3": P, "4": P, "5": P, "6": P, "7": P, "8": H, "9": H, "10": H, "A": H},
    }


    @classmethod
    def strategy(cls, player_hand: Hand, dealer_card: Card) -> Action:
        if not isinstance(player_hand, Hand):
            raise ValueError("player hand must be instance of Hand")
        
        if not isinstance(dealer_card, Card):
            raise ValueError("dealer card must be instance of Card")
        
        if len(player_hand) < 2:
            raise ValueError("player hand must have at least 2 cards")
        
        dealer_card_rank = dealer_card.rank
        if dealer_card.rank in ["J", "Q", "K"]:
            dealer_card_rank = "10" 
        
        #Pairs
        if len(player_hand) == 2 and BlackJackEval.can_split(player_hand):
            correct_move = cls.PAIR_STRATEGY[player_hand.cards[0].rank][dealer_card_rank]

            return correct_move
        
        #Softs
        if BlackJackEval.soft(player_hand):
            value = BlackJackEval.value(player_hand)
            correct_move = cls.SOFT_STRATEGY[value][dealer_card_rank]

            return correct_move
        
        #Hards
        value = BlackJackEval.value(player_hand)
        correct_move = cls.HARD_STRATEGY[value][dealer_card_rank]

        if correct_move == cls.Action.DOUBLE and len(player_hand) > 2:
            correct_move = cls.Action.HIT
        
        return correct_move
        
        