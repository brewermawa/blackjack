from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    """
    Defines an immutable playing card object with rank and suit attributes.

    Attributes
    rank:
    Represents the rank or face of the playing card
    Must be a string. TypeError if is anything other than str.
    The valid values of rank are: "A", "2", "3", "4", "5", "6", "7", "8",
    "9", "10", "J", "Q" and "K"
    ValueError if not a valid value

    suit:
    Represents the suit of the playing card
    Must be a string. TypeError if is anything other than str.
    The valid values of suit are: "♣", "♦", "♠", "♥"
    ValueError if not a valid value
    """
    VALID_RANKS = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Joker"}
    VALID_SUITS = {"♣", "♦", "♠", "♥", "🃏"}

    rank: str
    suit: str

    def __post_init__(self):
        if not isinstance(self.rank, str) or not isinstance(self.suit, str):
            raise TypeError("rank and suit must be of type string (str)") 
        
        if self.rank not in self.VALID_RANKS or self.suit not in self.VALID_SUITS:
            raise ValueError("rank and suit must have a valid value")
        
    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"{self.rank}{self.suit}"