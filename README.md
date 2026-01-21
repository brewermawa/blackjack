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


# BlackJackStrategy

The purpose of the BlackJackStrategy class is very simple: it receives the player hand and the dealers up card and returns the correct action (stand, hit, double, split, surrender).

It does nothing else: does not manipulate hands, calculate payouts, make a decision, etc.

It is meant to be used by other code, for example the blackjack simulator

No instances of BlackJackStrategy can be created (no __init__ method). The class will only expose class methods.

For v1.0 only one set of rules will be used:
- Dealer hits on soft 17
- Surrender
- Doble after split allowed
- Double with any two cards

The action returned is of type Action that is an Enum declared inside BlackJackStrategy:
class Action(Enum):
    HIT = "hit"
    STAND = "stand"
    DOUBLE = "double"
    SPLIT = "split"
    SURRENDER = "surrender"

## Methods (decorated with @classmethod)
strategy(player_hand: Hand, dealer_card: Card) -> BlackJackStrategy.Action:
The strategy method receives the player hand and the dealer up card and returns a value of the Action Enum defined inside the BlackJackStrategy class.

The strategy is based on the following table:
         2  3  4  5  6  7  8  9  10 A
5–8      H  H  H  H  H  H  H  H  H  H
9        H  D  D  D  D  H  H  H  H  H
10       D  D  D  D  D  D  D  D  H  H
11       D  D  D  D  D  D  D  D  D  H
12       H  H  S  S  S  H  H  H  H  H
13–14    S  S  S  S  S  H  H  H  H  H
15       S  S  S  S  S  H  H  H  R  H
16       S  S  S  S  S  H  H  R  R  R
17+      S  S  S  S  S  S  S  S  S  S

          2  3  4  5  6  7  8  9  10 A
A,2 (13)  H  H  H  D  D  H  H  H  H  H
A,3 (14)  H  H  H  D  D  H  H  H  H  H
A,4 (15)  H  H  D  D  D  H  H  H  H  H
A,5 (16)  H  H  D  D  D  H  H  H  H  H
A,6 (17)  H  D  D  D  D  H  H  H  H  H
A,7 (18)  S  D  D  D  D  S  S  H  H  H
A,8 (19)  S  S  S  S  D  S  S  S  S  S
A,9 (20)  S  S  S  S  S  S  S  S  S  S

         2  3  4  5  6  7  8  9  10 A
A,A      P  P  P  P  P  P  P  P  P  P
10,10    S  S  S  S  S  S  S  S  S  S
9,9      P  P  P  P  P  S  P  P  S  S
8,8      P  P  P  P  P  P  P  P  P  P
7,7      P  P  P  P  P  P  H  H  H  H
6,6      P  P  P  P  P  H  H  H  H  H
5,5      D  D  D  D  D  D  D  D  H  H
4,4      H  H  H  P  P  H  H  H  H  H
3,3      P  P  P  P  P  P  H  H  H  H
2,2      P  P  P  P  P  P  H  H  H  H

H = Hit
S = Stand
D = Double
P = Split
R = Surrender

Decision priority follows standard blackjack rules: pairs first, then soft totals, then hard totals.
