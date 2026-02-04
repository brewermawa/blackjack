import pytest

from enum import Enum

from roundoutcome import RoundOutcome


class TestOutcome:
    def test_roundoutcome_exists_and_can_be_imported(self):
        from roundoutcome import RoundOutcome


    def test_roundoutcome_is_subclass_of_enum(self):
        assert issubclass(RoundOutcome, Enum)


    def test_roundoutcome_has_exactly_seven_members(self):
        assert len(RoundOutcome) == 7


    def test_roundoutcome_contains_win_loss_push_blackjack(self):
        assert "WIN" in RoundOutcome.__members__
        assert "LOSS" in RoundOutcome.__members__
        assert "PUSH" in RoundOutcome.__members__
        assert "BLACKJACK" in RoundOutcome.__members__
        assert "DOUBLE_WIN" in RoundOutcome.__members__
        assert "DOUBLE_LOSS" in RoundOutcome.__members__


    @pytest.mark.parametrize(
        "invalid_value",
        ["WON", "LOST", "TIED", "BJ", None]
    )
    def test_roundoutcome_raises_valuerror_if_value_not_valid_member(self, invalid_value):
        with pytest.raises(ValueError):
            RoundOutcome(invalid_value)


    def test_roundoutcome_enum_values_are_all_distinct(self):
        assert len(RoundOutcome) == len({outcome.value for outcome in RoundOutcome})