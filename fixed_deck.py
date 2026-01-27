from cards.deck import Deck
from cards.card import Card

#["♣", "♦", "♠", "♥"]
class FixedDeck(Deck):
    _TEST_SUIT = "♦"  # suit fija para armar secuencias deterministas en tests

    def __init__(self, number_of_decks = 1, jokers = False):
        super().__init__(number_of_decks, jokers)
    
    def shuffle(self):
        super()._build_deck()

    def _take_one_by_rank(self, rank: str) -> Card:
        """
        Remove and return one existing card from the deck with the given rank.
        Suit is not constrained. Raises ValueError if not found.
        """
        for c in self._deck:
            if c.rank == rank:
                self._deck.remove(c)
                return c
        raise ValueError(f"No card with rank {rank} found in deck")

    def _program_ranks_top(self, ranks_in_draw_order: list[str]) -> None:
        """
        Arrange the deck so that successive draws (pop from end) return the given
        ranks in this exact order. Supports repeated ranks.
        """
        # Take actual cards (preserves multiplicity correctly)
        taken: list[Card] = [self._take_one_by_rank(r) for r in ranks_in_draw_order]

        # Append in reverse so the last appended is drawn first
        for c in reversed(taken):
            self._deck.append(c)


    def deck_for_bj(self):
        self._program_ranks_top(["A", "8", "K", "J"])

    def deck_for_win(self):
        self._program_ranks_top(["10", "6", "K", "9", "8"])

    def deck_for_loss(self):
        self._program_ranks_top(["9", "K", "8", "9"])

    def deck_for_push(self):
        self._program_ranks_top(["10", "9", "7", "8"])

    def deck_for_double_win(self):
        self._program_ranks_top(["5", "5", "6", "6", "10", "9"])

    def deck_for_double_loss(self):
        self._program_ranks_top(["9", "6", "2", "5", "9", "J"])

    def deck_for_split_push(self):
        self._program_ranks_top(["8", "9", "8", "9", "K", "Q"])

    def deck_for_split_win_both(self):
        self._program_ranks_top(["8", "6", "8", "10", "K", "Q", "9"])

    def deck_for_split_win_one_loose_one(self):
        self._program_ranks_top(["8", "6", "8", "10", "K", "9", "10"])

    def deck_for_split_AA(self):
        self._program_ranks_top(["A", "9", "A", "10", "5", "K"])

    def deck_for_split_then_double(self):
        self._program_ranks_top(["6", "5", "6", "10", "5", "K", "4", "K", "Q"])
