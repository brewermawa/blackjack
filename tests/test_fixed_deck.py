import pytest

from fixed_deck import FixedDeck

#["♣", "♦", "♠", "♥"]
class TestFixedDeck:
    def _draw_ranks(self, deck: FixedDeck, n: int) -> list[str]:
        return [deck.draw()[0].rank for _ in range(n)]

    def test_fixeddeck_shuffle_does_not_affect_order_of_cards(self):
        deck1 = FixedDeck()
        deck2 = FixedDeck()
        cards_deck1 = []
        cards_deck2 = []

        for _ in range(10):
            cards_deck1.append(deck1.draw()[0])

        deck2.shuffle()

        for _ in range(10):
            cards_deck2.append(deck2.draw()[0])
        
        assert [(c.rank, c.suit) for c in cards_deck1] == [(c.rank, c.suit) for c in cards_deck2]


    @pytest.mark.parametrize(
        "setup_method, expected_first_n_ranks",
        [
            ("deck_for_bj", ["A", "8", "K", "J"]),
            ("deck_for_win", ["10", "6", "K", "9", "8"]),
            ("deck_for_loss", ["9", "K", "8", "9"]),
            ("deck_for_push", ["10", "9", "7", "8"]),
            ("deck_for_double_win", ["5", "5", "6", "6", "10", "9"]),
            ("deck_for_double_loss", ["9", "6", "2", "5", "9", "J"]),
            ("deck_for_split_push", ["8", "9", "8", "9", "K", "Q"]),
            ("deck_for_split_win_both", ["8", "6", "8", "10", "K", "Q", "9"]),
            ("deck_for_split_win_one_loss_one", ["8", "8", "8", "9", "4", "9", "6", "10"]),
            ("deck_for_split_AA_win_win", ["A", "9", "A", "10", "J", "K"]),
        ],
    )
    def test_fixeddeck_scenarios_initial_order(self, setup_method: str, expected_first_n_ranks: list[str]):
        deck = FixedDeck()
        getattr(deck, setup_method)()
        assert self._draw_ranks(deck, len(expected_first_n_ranks)) == expected_first_n_ranks