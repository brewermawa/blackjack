# class BlackJackEval

The purpose of this class is to evaluate a blackjack hand. The methods will receive an instance of the hand class and return the appropriate response.

This class is not meant to be used to create instances, it will only contain class methods that do not need the class to be initialized, hence, no __init__ constructor method is created.


## Methods (all decorated with the @classmethod decorator. all methods have a hand parameter)

- blackjack(cls, hand: Hand) -> bool: verifies that the received hand is a blackjack. A blackjack is a hand of two cards: an "A" and either a "10", "J", "Q" or "K". Suits are irrelevant. Raises ValueError if the hand does not contain exactly 2 cards.

- can_double(cls, hand: Hand, valid_doubles: list=[]) -> bool: Some variants of blackjack require that the hand be a certain value to decide if the player can double (eg. 9, 10, 11). Receives the hand to evaluate and an optional list with valid double values. If the list is empty, can_double returns True (if there are exactly 2 cards), if the list is not empty, can_double checks if the value of the hand is in the valid_doubles list and returns True or False accordingly. Raises ValueError if valid_doubles is not a list. All the values in list must be integers, otherwise it raises ValueError. Raises ValueError if the hand does not contain exactly 2 cards. 

- can_split(cls, hand: Hand) -> bool: Receives the hand to evaluate. Returns True if the cards are of the same rank (pair). For blackjack, "10", "J", "Q" or "K", are considered the same rank (eg. a hand with a "10" and "J" is considered a pair). Return False otherwise. Suits are irrelevant. Raises ValueError if the hand does not contain exactly 2 cards.

- soft(cls, hand: Hand) -> bool: Receives the hand to evaluate. Returns True if the hand is "soft". A hand is soft if it contains an "A", the "A" is counted as 11 and the hand does not bust. Again, suits are irrelevant. By this definition, a blackjack is soft. If the hand contains more than one "A" only one of them can be considered an 11 and, if the hand does not bust, it is also soft. Returns True or False accordingly. Raises ValueError if the hand contains less than 2 cards.

- value(cls, hand: Hand) -> int: Returns the value (sum of ranks) of the hand. An "A" can have the values of 1 or 11. If a hand has an "A", it is first counted as 11, if the value is over 21, then we consider the "A" as 1 and return the value. In the case of having more than one "A", one of the "A" will be first considered an 11 and then a 1 if the value of the hand is over 21. Raises ValueError if the hand contains less than 2 cards.

- bust(cls, hand: Hand) -> bool: uses the value method. if value(hand) returns anything over 21 bust returns True. Otherwise it returns False. Raises ValueError if the hand contains less than 2 cards.

### Comments
- All of the methods should check if the hand received is an instance of the hand class and raise a ValueError if it is not.