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

    hand_a82 = Hand()
    hand_a82.add_card(Card("A", "♣"))
    hand_a82.add_card(Card("8", "♦"))
    hand_a82.add_card(Card("2", "♦"))
    
    hand_aa8 = Hand()
    hand_aa8.add_card(Card("A", "♣"))
    hand_aa8.add_card(Card("A", "♦"))
    hand_aa8.add_card(Card("8", "♣"))

    hand_aaa6 = Hand()
    hand_aaa6.add_card(Card("A", "♣"))
    hand_aaa6.add_card(Card("A", "♦"))
    hand_aaa6.add_card(Card("A", "♥"))
    hand_aaa6.add_card(Card("6", "♣"))

    hand_aaa9 = Hand()
    hand_aaa9.add_card(Card("A", "♣"))
    hand_aaa9.add_card(Card("A", "♦"))
    hand_aaa9.add_card(Card("A", "♥"))
    hand_aaa9.add_card(Card("9", "♣"))

    hand_bust_996 = Hand()
    hand_bust_996.add_card(Card("9", "♣"))
    hand_bust_996.add_card(Card("9", "♦"))
    hand_bust_996.add_card(Card("6", "♥"))
    
    hand_bust_93J = Hand()
    hand_bust_93J.add_card(Card("9", "♣"))
    hand_bust_93J.add_card(Card("3", "♦"))
    hand_bust_93J.add_card(Card("J", "♥"))

    hand_bust_AA46J = Hand()
    hand_bust_AA46J.add_card(Card("A", "♥"))
    hand_bust_AA46J.add_card(Card("A", "♦"))
    hand_bust_AA46J.add_card(Card("4", "♥"))
    hand_bust_AA46J.add_card(Card("6", "♥"))
    hand_bust_AA46J.add_card(Card("J", "♥"))

    # soft
    hand_A62 = Hand()
    hand_A62.add_card(Card("A","♣"))
    hand_A62.add_card(Card("6","♦"))
    hand_A62.add_card(Card("2","♦"))

    # soft
    hand_A222 = Hand()
    hand_A222.add_card(Card("A","♣"))
    hand_A222.add_card(Card("2","♦"))
    hand_A222.add_card(Card("2","♣"))
    hand_A222.add_card(Card("2","♥"))

    # not soft
    hand_A67 = Hand()
    hand_A67.add_card(Card("A","♣"))
    hand_A67.add_card(Card("6","♦"))
    hand_A67.add_card(Card("7","♣"))

    # not soft
    hand_A59 = Hand()
    hand_A59.add_card(Card("A","♣"))
    hand_A59.add_card(Card("5","♦"))
    hand_A59.add_card(Card("9","♣"))

    # not soft
    hand_A6T = Hand()
    hand_A6T.add_card(Card("A","♣"))
    hand_A6T.add_card(Card("6","♦"))
    hand_A6T.add_card(Card("J","♣"))

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
        [(9, 10, 11), {9, 10, 11}, 11, "11"]
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

    def test_can_double_returns_true_with_valid_doubles_list_set_and_hand_value_in_list(self):
        assert BlackJackEval.can_double(self.hand_83, [9, 10, 11]) is True

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

    @pytest.mark.parametrize(
        "hand",
        [hand_zero_cards, hand_one_card]
    )
    def test_soft_raises_valueerror_if_hand_contains_less_than_two_cards(self, hand):
        with pytest.raises(ValueError):
            BlackJackEval.soft(hand)

    @pytest.mark.parametrize(
        "hand_is_soft",
        [hand_a2, hand_a10, hand_a82, hand_aa8, hand_aaa6, hand_A222]
    )
    def test_soft_returns_true_if_the_hand_is_soft(self, hand_is_soft):
        assert BlackJackEval.soft(hand_is_soft) is True

    @pytest.mark.parametrize(
        "hand_not_soft",
        [hand_62, hand_66, hand_kj, hand_A67, hand_A59, hand_A6T]
    )
    def test_soft_returns_false_if_the_hand_is_not_soft(self, hand_not_soft):
        assert BlackJackEval.soft(hand_not_soft) is False

    @pytest.mark.parametrize(
        "hand",
        [hand_zero_cards, hand_one_card]
    )
    def test_value_raises_valueerror_if_hand_contains_less_than_two_cards(self, hand):
        with pytest.raises(ValueError):
            BlackJackEval.value(hand)

    @pytest.mark.parametrize(
        "hand, result",
        [
            (hand_k10, 20),
            (hand_a2, 13),
            (hand_a82, 21),
            (hand_aaa6, 19),
            (hand_aaa9, 12),
            (hand_bust_996, 24),
            (hand_bust_93J, 22),
            (hand_bust_AA46J, 22)
        ]
    )
    def test_value_returns_correct_value(self, hand, result):
        assert BlackJackEval.value(hand) == result

    @pytest.mark.parametrize(
        "hand",
        [hand_zero_cards, hand_one_card]
    )
    def test_bust_raises_valueerror_if_hand_contains_less_than_two_cards(self, hand):
        with pytest.raises(ValueError):
            BlackJackEval.bust(hand)

    @pytest.mark.parametrize(
        "hand_bust",
        [
            hand_bust_996,
            hand_bust_93J,
            hand_bust_AA46J
        ]
    )
    def test_bust_returns_true_when_hand_value_over_21(self, hand_bust):
        assert BlackJackEval.bust(hand_bust) is True

    @pytest.mark.parametrize(
        "hand",
        [
            hand_k10,
            hand_a2,
            hand_a82,
            hand_aaa6,
            hand_aaa9
        ]
    )
    def test_bust_returns_false_when_hand_value_less_than_or_equal_to_21(self, hand):
        assert BlackJackEval.bust(hand) is False


