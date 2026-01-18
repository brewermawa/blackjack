from cards.hand import Hand

class BlackJackEval:
    """
    - blackjack(cls, hand: Hand) -> bool
    - can_double(cls, hand: Hand, valid_doubles: list=[]) -> bool
    - can_split(cls, hand: Hand) -> bool
    - soft(cls, hand: Hand) -> bool
    - value(cls, hand: Hand) -> int
    - bust(cls, hand: Hand) -> bool
    """

    @classmethod
    def _validate_is_hand(cls, hand: Hand) -> None:
        if not isinstance(hand, Hand):
            raise ValueError("hand must be an instance of the Hand class")
    
    @classmethod
    def _validate_two_cards(cls, hand: Hand) -> None:
        if len(hand) != 2:
            raise ValueError("hand must contain exactly 2 cards")
        
    @classmethod
    def _validate_two_or_more_cards(cls, hand: Hand) -> None:
        if len(hand) < 2:
            raise ValueError("hand must contain 2 or more cards")

    @classmethod
    def blackjack(cls, hand: Hand) -> bool:
        cls._validate_is_hand(hand)
        cls._validate_two_cards(hand)
        
        #Check for blackjack
        ace_in_hand = any(card.rank == "A" for card in hand.cards)
        ten_in_hand = any(card.rank in ["10", "J", "Q", "K"] for card in hand.cards)

        return ace_in_hand and ten_in_hand


    @classmethod
    def can_double(cls, hand: Hand, valid_doubles: list = None) -> bool:
        cls._validate_is_hand(hand)
        cls._validate_two_cards(hand)

        if valid_doubles is None:
            valid_doubles = []
       
        #validate valid_doubles is a list
        if not isinstance(valid_doubles, list):
            raise ValueError("valid_doubles must be a list")
        
        #validate valid_doubles members are all ints
        for val in valid_doubles:
            if not isinstance(val, int) or isinstance(val, bool):
                raise ValueError("all valid_doubles members must be integers")
            
        if len(valid_doubles) ==  0:
            return True
        
        if cls.value(hand) in valid_doubles:
            return True
        
        return False


    @classmethod
    def can_split(cls, hand: Hand) -> bool:
        cls._validate_is_hand(hand)
        cls._validate_two_cards(hand)
        
        if hand.cards[0].rank == hand.cards[1].rank:
            return True
        
        if hand.cards[0].rank in ["10", "J", "Q", "K"] and hand.cards[1].rank in ["10", "J", "Q", "K"]:
            return True
        
        return False


    @classmethod
    def soft(cls, hand: Hand) -> bool:
        cls._validate_is_hand(hand)
        cls._validate_two_or_more_cards(hand)
        
        ace_in_hand = any(card.rank == "A" for card in hand.cards)

        if ace_in_hand and cls.value(hand) <= 21:
            return True
        
        return False

    @classmethod
    def value(cls, hand: Hand) -> int:
        cls._validate_is_hand(hand)
        cls._validate_two_or_more_cards(hand)
        
        #Replace J, Q and K with 10
        ranks_JQK_as_10 = ["10" if card.rank in ["J", "Q", "K"] else card.rank for card in hand.cards]
        ace_in_hand = any(rank == "A" for rank in ranks_JQK_as_10)

        if not ace_in_hand:
            ranks = [int(rank) for rank in ranks_JQK_as_10]
            return sum(ranks)
        
        #Ace in hand
        #Cast ranks as int, A's converted to 1
        ranks_int = [1 if rank == "A" else int(rank) for rank in ranks_JQK_as_10]

        if sum(ranks_int) + 10 <= 21:
            return sum(ranks_int) + 10
        else:
            return sum(ranks_int)


    @classmethod
    def bust(cls, hand: Hand) -> bool:
        cls._validate_is_hand(hand)
        cls._validate_two_or_more_cards(hand)

        return cls.value(hand) > 21