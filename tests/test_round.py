import pytest

from cards.deck import Deck
from blackjack.round import BlackJackRound
from blackjack.roundoutcome import RoundOutcome
from blackjack.fixed_deck import FixedDeck

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
    def test_raises_type_error_if_deck_is_not_instance_of_deck(self, deck):
        with pytest.raises(TypeError):
            BlackJackRound(deck, hits_soft_17=True)

    
    def test_raises_value_error_if_deck_contains_jokers(self):
        deck = FixedDeck(jokers=True)
        
        with pytest.raises(ValueError):
            BlackJackRound(deck, hits_soft_17=True)

    
    @pytest.mark.parametrize(
        "hits_soft_17_not_bool",
        ["True", None, 1.0, 1]
    )
    def test_raises_type_error_when_hits_soft_17_not_instance_of_bool(self, hits_soft_17_not_bool):
        deck = FixedDeck()

        with pytest.raises(TypeError):
            BlackJackRound(deck, hits_soft_17=hits_soft_17_not_bool)
            
    