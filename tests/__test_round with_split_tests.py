import pytest

from round import BlackJackRound
from roundoutcome import RoundOutcome
from cards.deck import Deck
from fixed_deck import FixedDeck

class TestRound:
    @pytest.mark.parametrize(
        "deck",
        [
            ["2♣", "A♥"],
            {"card1": {"rank": "A", "suit": "♥"}, "card2": {"rank": "7", "suit": "♥"}},
            [],
            None,
        ]
    )
    def test_raises_valueerror_if_deck_is_not_instance_of_deck(self, deck):
        with pytest.raises(ValueError):
            BlackJackRound(deck, hits_soft_17=True)

    
    def test_does_not_raise_valueerror_if_deck_is_instance_of_deck(self):
        deck = FixedDeck()
        BlackJackRound(deck, hits_soft_17=True)

    
    def test_raises_value_error_if_deck_contains_jokers(self):
        deck = FixedDeck(number_of_decks=2, jokers=True)
        
        with pytest.raises(ValueError):
            BlackJackRound(deck, hits_soft_17=True)

    
    @pytest.mark.parametrize(
        "hits_soft_17_not_bool",
        ["True", None, 1.0, 1]
    )
    def test_raises_valueerror_when_hits_soft_17_not_instance_of_bool(self, hits_soft_17_not_bool):
        deck = FixedDeck()

        with pytest.raises(ValueError):
            BlackJackRound(deck, hits_soft_17=hits_soft_17_not_bool)
            
    
    def test_player_and_dealer_hands_have_zero_cards_when_class_initialized(self):
        deck = FixedDeck()
        bj_round = BlackJackRound(deck, hits_soft_17=True)
        assert len(bj_round.player_hand) == 0
        assert len(bj_round.dealer_hand) == 0


    def test_play_returns_only_valid_roundoutcomes(self):
        VALID_VALUES = set(RoundOutcome)

        deck = FixedDeck()
        deck.deck_for_bj()

        bj_round = BlackJackRound(deck, hits_soft_17=True)
        results = bj_round.play()

        assert isinstance(results, list)
        assert len(results) == 1

        for r in results:
            assert r in VALID_VALUES



    @pytest.mark.parametrize(
        "setup_method",
        [
            "deck_for_bj",
            "deck_for_win"
        ]
    )
    def test_play_returns_list_with_one_outcome(self, setup_method):
        deck = FixedDeck()
        getattr(deck, setup_method)()

        bj_round = BlackJackRound(deck=deck, hits_soft_17=True)
        outcome = bj_round.play()

        assert len(outcome) == 1

    
    @pytest.mark.parametrize(
        "setup_method",
        [
            "deck_for_split_win_one_loose_one",
            "deck_for_split_AA",
        ]
    )
    def test_play_returns_list_with_two_outcomes_when_play_split(self, setup_method):
        deck = FixedDeck()
        getattr(deck, setup_method)()

        bj_round = BlackJackRound(deck=deck, hits_soft_17=True)
        outcome = bj_round.play()

        assert len(outcome) == 2


    @pytest.mark.parametrize(
        "setup_method, expected_outcomes",
        [
            ("deck_for_bj", [RoundOutcome.BLACKJACK]),
            ("deck_for_win", [RoundOutcome.WIN]),
            ("deck_for_loss", [RoundOutcome.LOSS]),
            ("deck_for_push", [RoundOutcome.PUSH]),
            ("deck_for_double_win", [RoundOutcome.DOUBLE_WIN]),
            ("deck_for_double_loss", [RoundOutcome.DOUBLE_LOSS]),
            ("deck_for_split_push", [RoundOutcome.PUSH, RoundOutcome.PUSH]),
            ("deck_for_split_win_both", [RoundOutcome.WIN, RoundOutcome.WIN]),
            ("deck_for_split_win_one_loose_one", [RoundOutcome.WIN, RoundOutcome.LOSS]),
            ("deck_for_split_AA", [RoundOutcome.WIN, RoundOutcome.WIN]),
            ("deck_for_split_then_double", [RoundOutcome.DOUBLE_WIN, RoundOutcome.DOUBLE_WIN]),
        ]
    )
    def test_play_returns_expected_outcome_for_fixed_scenarios(self, setup_method, expected_outcomes):
        deck = FixedDeck()
        getattr(deck, setup_method)()

        bj_round = BlackJackRound(deck=deck, hits_soft_17=True)
        outcomes = bj_round.play()

        assert outcomes == expected_outcomes
