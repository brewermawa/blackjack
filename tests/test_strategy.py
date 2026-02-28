import pytest

from fixed_deck import FixedDeck
from cards.hand import Hand
from roundoutcome import RoundOutcome
from strategy import BlackJackStrategy
from cards.card import Card
from cards.hand import Hand
from round import BlackJackRound

class TestBlackJackStrategy:
    #"♣", "♦", "♠", "♥"
    hand_zero_cards = Hand()

    hand_one_card = Hand()
    hand_one_card.add_card(Card("A", "♣"))

    valid_hand = Hand()
    valid_hand.add_card(Card("A", "♣"))
    valid_hand.add_card(Card("2", "♦"))
    
    # 5–8
    hand_32 = Hand(); hand_32.add_card(Card("3","♣")); hand_32.add_card(Card("2","♦"))
    hand_52 = Hand(); hand_52.add_card(Card("5","♣")); hand_52.add_card(Card("2","♦"))
    hand_62 = Hand(); hand_62.add_card(Card("6","♣")); hand_62.add_card(Card("2","♦"))
    hand_53 = Hand(); hand_53.add_card(Card("5","♣")); hand_53.add_card(Card("3","♦"))
    hand_44 = Hand(); hand_44.add_card(Card("4","♣")); hand_44.add_card(Card("4","♦"))

    # 9
    hand_63 = Hand(); hand_63.add_card(Card("6","♣")); hand_63.add_card(Card("3","♦"))

    # 10
    hand_82 = Hand(); hand_82.add_card(Card("8","♣")); hand_82.add_card(Card("2","♦"))

    # 11
    hand_92 = Hand(); hand_92.add_card(Card("9","♣")); hand_92.add_card(Card("2","♦"))

    # 12
    hand_84 = Hand(); hand_84.add_card(Card("8","♣")); hand_84.add_card(Card("4","♦"))

    # 13–14
    hand_85 = Hand(); hand_85.add_card(Card("8","♣")); hand_85.add_card(Card("5","♦"))
    hand_96 = Hand(); hand_96.add_card(Card("9","♣")); hand_96.add_card(Card("6","♦"))

    # 15
    hand_96 = Hand(); hand_96.add_card(Card("9","♣")); hand_96.add_card(Card("6","♦"))

    # 16
    hand_97 = Hand(); hand_97.add_card(Card("9","♣")); hand_97.add_card(Card("7","♦"))

    # 17+
    hand_98 = Hand(); hand_98.add_card(Card("9","♣")); hand_98.add_card(Card("8","♦"))
    hand_99 = Hand(); hand_99.add_card(Card("9","♣")); hand_99.add_card(Card("9","♦"))

    hand_A2 = Hand(); hand_A2.add_card(Card("A","♣")); hand_A2.add_card(Card("2","♦"))
    hand_A3 = Hand(); hand_A3.add_card(Card("A","♣")); hand_A3.add_card(Card("3","♦"))
    hand_A4 = Hand(); hand_A4.add_card(Card("A","♣")); hand_A4.add_card(Card("4","♦"))
    hand_A5 = Hand(); hand_A5.add_card(Card("A","♣")); hand_A5.add_card(Card("5","♦"))
    hand_A6 = Hand(); hand_A6.add_card(Card("A","♣")); hand_A6.add_card(Card("6","♦"))
    hand_A7 = Hand(); hand_A7.add_card(Card("A","♣")); hand_A7.add_card(Card("7","♦"))
    hand_A8 = Hand(); hand_A8.add_card(Card("A","♣")); hand_A8.add_card(Card("8","♦"))
    hand_A9 = Hand(); hand_A9.add_card(Card("A","♣")); hand_A9.add_card(Card("9","♦"))

    hand_AA = Hand(); hand_AA.add_card(Card("A","♣")); hand_AA.add_card(Card("A","♦"))
    hand_22 = Hand(); hand_22.add_card(Card("2","♣")); hand_22.add_card(Card("2","♦"))
    hand_33 = Hand(); hand_33.add_card(Card("3","♣")); hand_33.add_card(Card("3","♦"))
    hand_44 = Hand(); hand_44.add_card(Card("4","♣")); hand_44.add_card(Card("4","♦"))
    hand_55 = Hand(); hand_55.add_card(Card("5","♣")); hand_55.add_card(Card("5","♦"))
    hand_66 = Hand(); hand_66.add_card(Card("6","♣")); hand_66.add_card(Card("6","♦"))
    hand_77 = Hand(); hand_77.add_card(Card("7","♣")); hand_77.add_card(Card("7","♦"))
    hand_88 = Hand(); hand_88.add_card(Card("8","♣")); hand_88.add_card(Card("8","♦"))
    hand_99 = Hand(); hand_99.add_card(Card("9","♣")); hand_99.add_card(Card("9","♦"))
    hand_TT = Hand(); hand_TT.add_card(Card("10","♣")); hand_TT.add_card(Card("K","♦"))

    # hands with 3 or more cards
    hand_234 = Hand()
    hand_234.add_card(Card("2","♣"))
    hand_234.add_card(Card("3","♦"))
    hand_234.add_card(Card("4","♦"))

    hand_T27 = Hand()
    hand_T27.add_card(Card("J","♣"))
    hand_T27.add_card(Card("2","♦"))
    hand_T27.add_card(Card("7","♦"))

    # soft hands with 3 or more cards
    hand_A62 = Hand()
    hand_A62.add_card(Card("A","♣"))
    hand_A62.add_card(Card("6","♦"))
    hand_A62.add_card(Card("2","♦"))

    hand_A222 = Hand()
    hand_A222.add_card(Card("A","♣"))
    hand_A222.add_card(Card("2","♦"))
    hand_A222.add_card(Card("2","♣"))
    hand_A222.add_card(Card("2","♥"))

    hand_A67 = Hand()
    hand_A67.add_card(Card("A","♣"))
    hand_A67.add_card(Card("6","♦"))
    hand_A67.add_card(Card("7","♣"))

    hand_A59 = Hand()
    hand_A59.add_card(Card("A","♣"))
    hand_A59.add_card(Card("5","♦"))
    hand_A59.add_card(Card("9","♣"))

    hand_A6T = Hand()
    hand_A6T.add_card(Card("A","♣"))
    hand_A6T.add_card(Card("6","♦"))
    hand_A6T.add_card(Card("J","♣"))

    hand_T24 = Hand()
    hand_T24.add_card(Card("J","♣"))
    hand_T24.add_card(Card("2","♦"))
    hand_T24.add_card(Card("4","♣"))


    dealer_2  = Card("2","♣")
    dealer_3  = Card("3","♣")
    dealer_4  = Card("4","♣")
    dealer_5  = Card("5","♣")
    dealer_6  = Card("6","♣")
    dealer_7  = Card("7","♣")
    dealer_8  = Card("8","♣")
    dealer_9  = Card("9","♣")
    dealer_10 = Card("10","♣")
    dealer_J = Card("J", "♣")
    dealer_Q = Card("Q", "♣")
    dealer_K = Card("K", "♣")
    dealer_A  = Card("A","♣")


    @pytest.mark.parametrize(
        "invalid_hand",
        [
            (Card("A", "♣"), Card("8", "♦")),
            [Card("A", "♣"), Card("8", "♦")],
            {"card1": Card("A", "♣"), "card2": Card("8", "♣")},
            Card("A", "♣"),
            None,
        ], 
    )
    def test_strategy_raises_valueerror_if_player_hand_is_not_instance_of_hand(self, invalid_hand):
        with pytest.raises(ValueError):
            BlackJackStrategy.strategy(invalid_hand, Card("A", "♣"))

    @pytest.mark.parametrize(
        "not_card",
        [
            {"rank": "A", "suit": "♣"},
            "A♣",
            ["A", "♣"],
            ("A", "♣"),
            None,
        ]
    )
    def test_strategy_raises_valueerror_if_dealer_card_is_not_instance_of_card(self, not_card):
        with pytest.raises(ValueError):
            BlackJackStrategy.strategy(self.valid_hand, not_card)

    @pytest.mark.parametrize(
        "hand",
        [hand_zero_cards, hand_one_card]
    )
    def test_strategy_raises_valueerror_if_player_hand_contains_less_than_two_cards(self, hand):
        with pytest.raises(ValueError):
            BlackJackStrategy.strategy(hand, Card("A", "♣"))

    def test_strategy_return_is_type_action(self):
        assert isinstance(BlackJackStrategy.strategy(self.valid_hand, Card("A", "♣")), BlackJackStrategy.Action)

    @pytest.mark.parametrize(
        "player_hand, dealer_card, expected",
        [
            #5-8 always hit
            (hand_32, dealer_6, BlackJackStrategy.Action.HIT),
            (hand_53, dealer_2, BlackJackStrategy.Action.HIT),
            (hand_53, dealer_J, BlackJackStrategy.Action.HIT),

            #double down
            (hand_63, dealer_5, BlackJackStrategy.Action.DOUBLE),
            (hand_82, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_82, dealer_9, BlackJackStrategy.Action.DOUBLE),
            (hand_92, dealer_3, BlackJackStrategy.Action.DOUBLE),
            (hand_92, dealer_10, BlackJackStrategy.Action.DOUBLE),
            (hand_92, dealer_Q, BlackJackStrategy.Action.DOUBLE),

            #edge cases double down
            (hand_63, dealer_2, BlackJackStrategy.Action.HIT),
            (hand_63, dealer_7, BlackJackStrategy.Action.HIT),
            (hand_82, dealer_10, BlackJackStrategy.Action.HIT),
            (hand_92, dealer_A, BlackJackStrategy.Action.HIT),

            #player hand 12
            (hand_84, dealer_3, BlackJackStrategy.Action.HIT),
            (hand_84, dealer_4, BlackJackStrategy.Action.STAND),
            (hand_84, dealer_6, BlackJackStrategy.Action.STAND),
            (hand_84, dealer_7, BlackJackStrategy.Action.HIT),

            #player hand 13-16
            (hand_85, dealer_6, BlackJackStrategy.Action.STAND),
            (hand_85, dealer_7, BlackJackStrategy.Action.HIT),
            (hand_96, dealer_6, BlackJackStrategy.Action.STAND),
            (hand_96, dealer_7, BlackJackStrategy.Action.HIT),
            
            #surrender or close
            (hand_96, dealer_9, BlackJackStrategy.Action.HIT),
            (hand_96, dealer_10, BlackJackStrategy.Action.SURRENDER),
            (hand_96, dealer_A, BlackJackStrategy.Action.HIT),
            (hand_97, dealer_9, BlackJackStrategy.Action.SURRENDER),
            (hand_97, dealer_10, BlackJackStrategy.Action.SURRENDER),
            (hand_97, dealer_K, BlackJackStrategy.Action.SURRENDER),
            (hand_97, dealer_A, BlackJackStrategy.Action.SURRENDER),

            #17+
            (hand_98, dealer_6, BlackJackStrategy.Action.STAND),
            (hand_98, dealer_7, BlackJackStrategy.Action.STAND),
            (hand_98, dealer_10, BlackJackStrategy.Action.STAND),
            (hand_98, dealer_A, BlackJackStrategy.Action.STAND),

            #three or more cards
            #hand_234: 9 against a 6 should be DOUBLE, but because we have 3 cards,
            #and doubles are permitted only on two cards, should return HIT.
            (hand_234, dealer_6, BlackJackStrategy.Action.HIT),
            (hand_T27, dealer_6, BlackJackStrategy.Action.STAND)
        ]
    )
    def test_strategy_returns_correct_action_with_hard_hands(self, player_hand, dealer_card, expected):
        assert BlackJackStrategy.strategy(player_hand, dealer_card) == expected

    @pytest.mark.parametrize(
        "player_hand, dealer_card, expected",
        [
            (hand_A2, dealer_4, BlackJackStrategy.Action.HIT),
            (hand_A2, dealer_5, BlackJackStrategy.Action.DOUBLE),
            (hand_A2, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_A2, dealer_7, BlackJackStrategy.Action.HIT),

            (hand_A3, dealer_4, BlackJackStrategy.Action.HIT),
            (hand_A3, dealer_5, BlackJackStrategy.Action.DOUBLE),
            (hand_A3, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_A3, dealer_7, BlackJackStrategy.Action.HIT),

            (hand_A4, dealer_3, BlackJackStrategy.Action.HIT),
            (hand_A4, dealer_4, BlackJackStrategy.Action.DOUBLE),
            (hand_A4, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_A4, dealer_7, BlackJackStrategy.Action.HIT),

            (hand_A5, dealer_3, BlackJackStrategy.Action.HIT),
            (hand_A5, dealer_4, BlackJackStrategy.Action.DOUBLE),
            (hand_A5, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_A5, dealer_7, BlackJackStrategy.Action.HIT),

            (hand_A6, dealer_2, BlackJackStrategy.Action.HIT),
            (hand_A6, dealer_3, BlackJackStrategy.Action.DOUBLE),
            (hand_A6, dealer_4, BlackJackStrategy.Action.DOUBLE),
            (hand_A6, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_A6, dealer_7, BlackJackStrategy.Action.HIT),

            (hand_A7, dealer_2, BlackJackStrategy.Action.STAND),
            (hand_A7, dealer_3, BlackJackStrategy.Action.DOUBLE),
            (hand_A7, dealer_4, BlackJackStrategy.Action.DOUBLE),
            (hand_A7, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_A7, dealer_7, BlackJackStrategy.Action.STAND),
            (hand_A7, dealer_8, BlackJackStrategy.Action.STAND),
            (hand_A7, dealer_9, BlackJackStrategy.Action.HIT),

            (hand_A8, dealer_2, BlackJackStrategy.Action.STAND),
            (hand_A8, dealer_3, BlackJackStrategy.Action.STAND),
            (hand_A8, dealer_5, BlackJackStrategy.Action.STAND),
            (hand_A8, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_A8, dealer_7, BlackJackStrategy.Action.STAND),
            (hand_A8, dealer_8, BlackJackStrategy.Action.STAND),
            (hand_A8, dealer_9, BlackJackStrategy.Action.STAND),


            (hand_A9, dealer_2, BlackJackStrategy.Action.STAND),
            (hand_A9, dealer_6, BlackJackStrategy.Action.STAND),
            (hand_A9, dealer_7, BlackJackStrategy.Action.STAND),
            (hand_A9, dealer_9, BlackJackStrategy.Action.STAND),

            (hand_A62, dealer_9, BlackJackStrategy.Action.STAND),
            (hand_A222, dealer_9, BlackJackStrategy.Action.HIT),
            (hand_A67, dealer_9, BlackJackStrategy.Action.HIT),
            (hand_A59, dealer_9, BlackJackStrategy.Action.HIT),
            (hand_A6T, dealer_9, BlackJackStrategy.Action.STAND),
        ]
    )
    def test_strategy_returns_correct_action_with_soft_hands(self, player_hand, dealer_card, expected):
        assert BlackJackStrategy.strategy(player_hand, dealer_card) == expected

    @pytest.mark.parametrize(
        "player_hand, dealer_card, expected",
        [
            (hand_AA, dealer_2, BlackJackStrategy.Action.SPLIT),
            (hand_AA, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_AA, dealer_10, BlackJackStrategy.Action.SPLIT),
            (hand_AA, dealer_A, BlackJackStrategy.Action.SPLIT),

            (hand_TT, dealer_2, BlackJackStrategy.Action.STAND),
            (hand_TT, dealer_6, BlackJackStrategy.Action.STAND),
            (hand_TT, dealer_10, BlackJackStrategy.Action.STAND),
            (hand_TT, dealer_A, BlackJackStrategy.Action.STAND),

            (hand_99, dealer_2, BlackJackStrategy.Action.SPLIT),
            (hand_99, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_99, dealer_7, BlackJackStrategy.Action.STAND),
            (hand_99, dealer_8, BlackJackStrategy.Action.SPLIT),
            (hand_99, dealer_9, BlackJackStrategy.Action.SPLIT),
            (hand_99, dealer_10, BlackJackStrategy.Action.STAND),
            (hand_99, dealer_A, BlackJackStrategy.Action.STAND),

            (hand_88, dealer_2, BlackJackStrategy.Action.SPLIT),
            (hand_88, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_88, dealer_8, BlackJackStrategy.Action.SPLIT),
            (hand_88, dealer_10, BlackJackStrategy.Action.SPLIT),
            (hand_88, dealer_A, BlackJackStrategy.Action.SPLIT),

            (hand_77, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_77, dealer_7, BlackJackStrategy.Action.SPLIT),
            (hand_77, dealer_8, BlackJackStrategy.Action.HIT),
            (hand_77, dealer_9, BlackJackStrategy.Action.HIT),

            (hand_66, dealer_5, BlackJackStrategy.Action.SPLIT),
            (hand_66, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_66, dealer_7, BlackJackStrategy.Action.HIT),
            (hand_66, dealer_8, BlackJackStrategy.Action.HIT),

            (hand_55, dealer_2, BlackJackStrategy.Action.DOUBLE),
            (hand_55, dealer_4, BlackJackStrategy.Action.DOUBLE),
            (hand_55, dealer_6, BlackJackStrategy.Action.DOUBLE),
            (hand_55, dealer_8, BlackJackStrategy.Action.DOUBLE),
            (hand_55, dealer_9, BlackJackStrategy.Action.DOUBLE),
            (hand_55, dealer_10, BlackJackStrategy.Action.HIT),
            (hand_55, dealer_A, BlackJackStrategy.Action.HIT),

            (hand_44, dealer_4, BlackJackStrategy.Action.HIT),
            (hand_44, dealer_5, BlackJackStrategy.Action.SPLIT),
            (hand_44, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_44, dealer_7, BlackJackStrategy.Action.HIT),

            (hand_33, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_33, dealer_7, BlackJackStrategy.Action.SPLIT),
            (hand_33, dealer_8, BlackJackStrategy.Action.HIT),
            (hand_33, dealer_9, BlackJackStrategy.Action.HIT),

            (hand_22, dealer_6, BlackJackStrategy.Action.SPLIT),
            (hand_22, dealer_7, BlackJackStrategy.Action.SPLIT),
            (hand_22, dealer_8, BlackJackStrategy.Action.HIT),
            (hand_22, dealer_9, BlackJackStrategy.Action.HIT),
        ]
    )
    def test_strategy_returns_correct_action_with_pair_hands(self, player_hand, dealer_card, expected):
        assert BlackJackStrategy.strategy(player_hand, dealer_card) == expected


    def test_strategy_returns_hit_when_surrender_and_more_than_2_cards(self):
        assert BlackJackStrategy.strategy(self.hand_T24, self.dealer_Q) == BlackJackStrategy.Action.HIT

