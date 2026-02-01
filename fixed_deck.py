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

    def deck_for_win_with_hit(self):
        self._program_ranks_top(["10", "8", "2", "9", "8"])

    def deck_for_loss(self):
        self._program_ranks_top(["9", "K", "8", "9"])

    def deck_for_bust_after_hit(self):
        self._program_ranks_top(["9", "8", "6", "9", "Q"])

    def deck_for_push(self):
        self._program_ranks_top(["10", "9", "7", "8"])

    def deck_for_double_win(self):
        self._program_ranks_top(["5", "5", "6", "6", "10", "9"])

    def deck_for_double_loss(self):
        self._program_ranks_top(["9", "6", "2", "5", "9", "J"])

    def deck_for_double_push(self):
        self._program_ranks_top(["9", "9", "2", "2", "Q", "K"])

    def deck_for_surrender(self):
        self._program_ranks_top(["9", "K", "7", "6"])

    def deck_for_dealer_bust(self):
        self._program_ranks_top(["9", "9", "6", "7", "6", "Q"])

    def deck_for_dealer_bj(self):
        self._program_ranks_top(["9", "A", "6", "K", "6", "Q"])

    def deck_for_bj_push(self):
        self._program_ranks_top(["Q", "A", "A", "10", "6", "Q"])

    def deck_for_soft_hits_17_false_push(self):
        self._program_ranks_top(["Q", "A", "7", "6", "6", "Q"])

    def deck_for_soft_hits_17_true_player_wins(self):
        self._program_ranks_top(["Q", "A", "7", "6", "6", "Q"])

    def deck_for_soft_hits_17_true_player_loss(self):
        self._program_ranks_top(["Q", "A", "7", "6", "4", "Q"])

    def deck_for_soft_hits_17_true_push(self):
        self._program_ranks_top(["Q", "A", "7", "6", "10", "Q"])

    def deck_for_player_bust(self):
        self._program_ranks_top(["10", "7", "6", "Q", "10"])

    def deck_for_player_double_loss(self):
        self._program_ranks_top(["5", "8", "5", "Q", "7"])

    def deck_for_win_with_two_hits(self):
        self._program_ranks_top(["5", "8", "2", "Q", "3", "K"])

    def deck_for_loss_with_two_hits(self):
        self._program_ranks_top(["5", "8", "2", "Q", "3", "7"])

    def deck_for_split_win_one_loss_one(self):
        """
        dealer_hand: 8, 9
        player_hand[0]: 8, 4, 9 -> WIN
        player_hand[1]: 8, 6, 10 -> LOSS
        """
        self._program_ranks_top(["8", "8", "8", "9", "4", "9", "6", "10"])


    def deck_for_split_push(self):
        self._program_ranks_top(["8", "9", "8", "9", "K", "Q"])

    def deck_for_split_win_both(self):
        self._program_ranks_top(["8", "6", "8", "10", "K", "Q", "9"])

    def deck_for_split_win_one_loose_one(self):
        self._program_ranks_top(["8", "6", "8", "10", "K", "9", "10"])

    def deck_for_split_AA_win_win(self):
        """
        blackjack after split is otcome WIN not BLACKJACK"
        dealer_hand: 9, 10
        player_hand[0]: A, J
        player_hand[1]: A, K
        """
        self._program_ranks_top(["A", "9", "A", "10", "J", "K"])

    def deck_for_split_AA_only_one_extra_card_per_hand(self):
        """
        dealer_hand: 8, 9
        player_hand[0]: A, 5
        player_hand[1]: A, 4
        """
        self._program_ranks_top(["A", "8", "A", "9", "5", "4"])

    def deck_for_split_then_double(self):
        """
        dealer_hand: 5, 10
        player_hand[0]: 6, 5 (strategy returns double -> ValueError)
        player_hand[1]: 6
        """
        self._program_ranks_top(["6", "5", "6", "10", "5"])

    def deck_for_split_then_surrender(self):
        """
        dealer_hand: 10, 5
        player_hand[0]: 6, 10 (strategy returns surrender -> ValueError)
        player_hand[1]: 6
        """
        self._program_ranks_top(["6", "10", "6", "5", "10"])

    def deck_for_split_then_resplit(self):
        """
        dealer_hand: 5, 10
        player_hand[0]: 6, 6 (strategy returns split -> ValueError)
        player_hand[1]: 6
        """
        self._program_ranks_top(["6", "5", "6", "10", "6"])

