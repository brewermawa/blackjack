import pytest

from enum import Enum

from blackjack.roundoutcome import RoundOutcome


class TestOutcome:
    def test_roundoutcome_is_subclass_of_enum(self):
        assert issubclass(RoundOutcome, Enum)


    def test_roundoutcome_contains_win_loss_push_blackjack(self):
        assert "WIN" in RoundOutcome.__members__
        assert "LOSS" in RoundOutcome.__members__
        assert "PUSH" in RoundOutcome.__members__
        assert "BLACKJACK" in RoundOutcome.__members__
        assert "DOUBLE_WIN" in RoundOutcome.__members__
        assert "DOUBLE_LOSS" in RoundOutcome.__members__
        assert "HALF_PAY" in RoundOutcome.__members__
