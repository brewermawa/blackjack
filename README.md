# class BlackJackEval

The purpose of this class is to evaluate a black jack hand. The methods will receive an instance of the hand class and return the appropriate response.

This class is not meant to be used to create instances, it will only contain class methods that do not need the class to be initialized, hence, no __init__ constructor method is created.


## Methods (all decorated with the @classmethod decorator. all methods have a hand parameter)

- blackjack(cls, hand: Hand) -> bool: verifies that the received hand is a black jack. A black jack is a hand of two cards: an "A" and either a "10", "J", "Q" or "K". Suits are irrelevant. Raises ValueError if the hand does not contain exactly 2 cards.

- can_double(cls, hand: Hand, valid_doubles: list=[]): -> bool: Some variants of black jack require that the hand be a certain value to decide if the player can double (eg. 9, 10, 11). Recives the hand to evaluate and an optional list with valid double values. If the list is empty, can_double returns True (if there are exactly 2 cards), if the list is not empty, can_doulbe checks if the value of the hand is in the valid_doubles list and returns True of False accordingly. Raises ValueError if the hand does not contain exactly 2 cards.

- can_split(cls, hand: Hand) -> bool: Recives the hand to evaluate. Returns True if the cards are of the same rank (pair). For black jack, "10", "J", "Q" or "K", are considered the same rank (eg. a hand with a "10" and "J" is considered a pair). Return False otherwise. Suits are irrelevant.

- soft(cls, hand: Hand) -> bool: