import pytest

from blackjack_eval import BlackJackEval
from cards.card import Card
from cards.hand import Hand

"""
- blackjack(cls, hand: Hand) -> bool
- can_double(cls, hand: Hand, valid_doubles: list=[]) -> bool
- can_split(cls, hand: Hand) -> bool
- soft(cls, hand: Hand) -> bool
- value(cls, hand: Hand) -> int
- bust(cls, hand: Hand) -> bool
"""

class TestBlackjackEvalTypeValidation:
    @pytest.mark.parametrize(
        "method_to_test",
        [
            BlackJackEval.blackjack,
            BlackJackEval.can_double,
            BlackJackEval.can_split,
            BlackJackEval.soft,
            BlackJackEval.value,
            BlackJackEval.bust,
        ],
        ids=[
            "blackjack",
            "can_double",
            "can_split",
            "soft",
            "value",
            "bust",
        ],
    )
    @pytest.mark.parametrize(
        "invalid_hand",
        [
            {"card1": Card("A", "♣"), "card2": Card("J", "♦")},
            Card("J", "♦"),
            (("A", "♣"), ("J", "♦")),
            None,
            True
        ],
        ids=[
            "dict",
            "card",
            "tuple",
            "none",
            "bool",
        ]
    )
    def test_all_methods_raise_value_error_if_hand_not_hand_instance(self, method_to_test, invalid_hand):
        with pytest.raises(ValueError):
            method_to_test(invalid_hand)

class TestBlackjackEval:
    hand_zero_cards = Hand()

    hand_one_card = Hand()
    hand_one_card.add_card(Card("A", "♣"))

    hand_three_cards = Hand()
    hand_three_cards.add_card(Card("A", "♣"))
    hand_three_cards.add_card(Card("J", "♦"))
    hand_three_cards.add_card(Card("8", "♦"))

    hand_ak = Hand()
    hand_ak.add_card(Card("A", "♣"))
    hand_ak.add_card(Card("K", "♣"))

    hand_aq = Hand()
    hand_aq.add_card(Card("A", "♣"))
    hand_aq.add_card(Card("Q", "♦"))

    hand_aj = Hand()
    hand_aj.add_card(Card("A", "♣"))
    hand_aj.add_card(Card("J", "♣"))

    hand_a10 = Hand()
    hand_a10.add_card(Card("A", "♣"))
    hand_a10.add_card(Card("10", "♦"))

    hand_aa = Hand()
    hand_aa.add_card(Card("A", "♣"))
    hand_aa.add_card(Card("A", "♦"))

    hand_a2 = Hand()
    hand_a2.add_card(Card("A", "♣"))
    hand_a2.add_card(Card("2", "♦"))

    hand_kj = Hand()
    hand_kj.add_card(Card("K", "♣"))
    hand_kj.add_card(Card("J", "♦"))

    hand_87 = Hand()
    hand_87.add_card(Card("8", "♣"))
    hand_87.add_card(Card("7", "♦"))

    hand_83 = Hand()
    hand_83.add_card(Card("8", "♣"))
    hand_83.add_card(Card("3", "♦"))

    hand_62 = Hand()
    hand_62.add_card(Card("6", "♣"))
    hand_62.add_card(Card("2", "♦"))

    hand_66 = Hand()
    hand_66.add_card(Card("6", "♣"))
    hand_66.add_card(Card("6", "♦"))

    hand_k10 = Hand()
    hand_k10.add_card(Card("K", "♣"))
    hand_k10.add_card(Card("10", "♦"))

    @pytest.mark.parametrize(
        "hand",
        [hand_zero_cards, hand_one_card, hand_three_cards]
    )
    def test_blackjack_raises_valueerror_if_hand_does_not_contain_exactly_two_cards(self, hand):
        with pytest.raises(ValueError):
            BlackJackEval.blackjack(hand)
    
    @pytest.mark.parametrize(
        "hand",
        [hand_ak, hand_aq, hand_aj, hand_a10]
    )
    def test_blackjack_returns_true_with_valid_blackjack_hand(self, hand):
        assert BlackJackEval.blackjack(hand) is True

    @pytest.mark.parametrize(
        "hand",
        [hand_aa, hand_a2, hand_kj, hand_87]
    )
    def test_blackjack_returns_false_with_invalid_blackjack_hand(self, hand):
        assert BlackJackEval.blackjack(hand) is False

    @pytest.mark.parametrize(
        "hand",
        [hand_zero_cards, hand_one_card, hand_three_cards]
    )
    def test_can_double_raises_valueerror_if_hand_does_not_contain_exactly_two_cards(self, hand):
        with pytest.raises(ValueError):
            BlackJackEval.can_double(hand)

    @pytest.mark.parametrize(
        "valid_doubles_not_list",
        [(9, 10, 11), {9, 10, 11}, 11, "11", None]
    )
    def test_can_double_raises_valueerror_if_valid_doubles_is_not_list(self, valid_doubles_not_list):
        with pytest.raises(ValueError):
            BlackJackEval.can_double(self.hand_83, valid_doubles_not_list)

    @pytest.mark.parametrize(
        "valid_doubles_not_integer",
        [[9, "10", 11], [9, 10, 11.0], [True, False]]
    )
    def test_can_double_raises_valueerror_if_valid_doubles_list_member_is_not_int(self, valid_doubles_not_integer):
        with pytest.raises(ValueError):
            BlackJackEval.can_double(self.hand_83, valid_doubles_not_integer)

    def test_can_double_returns_true_with_valid_doubles_list_empty(self):
        assert BlackJackEval.can_double(self.hand_87) is True

    def test_can_double_returns_false_with_valid_doubles_list_set_and_hand_value_not_in_list(self):
        assert BlackJackEval.can_double(self.hand_62, [9, 10, 11]) is False

    @pytest.mark.parametrize(
        "hand",
        [hand_zero_cards, hand_one_card, hand_three_cards]
    )
    def test_can_split_raises_valueerror_if_hand_does_not_contain_exactly_two_cards(self, hand):
        with pytest.raises(ValueError):
            BlackJackEval.can_split(hand)

    @pytest.mark.parametrize(
        "hand_has_pair",
        [hand_k10, hand_66]
    )
    def test_can_split_returns_true_if_the_ranks_in_hand_are_pair(self, hand_has_pair):
        assert BlackJackEval.can_split(hand_has_pair) is True

    @pytest.mark.parametrize(
        "hand_not_pair",
        [hand_62, hand_83]
    )
    def test_can_split_returns_false_if_the_ranks_in_hand_are_not_pair(self, hand_not_pair):
        assert BlackJackEval.can_split(hand_not_pair) is False
