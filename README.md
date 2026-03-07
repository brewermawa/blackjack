# class BlackJackEval
- The purpose of this class is to evaluate a blackjack hand. The methods will receive an instance of the hand class and return the appropriate response.
- This class is not meant to be used to create instances, it will only contain class methods that do not need the class to be initialized. No __init__ constructor method is created.


## Methods (all decorated with the @classmethod decorator. all methods have a hand parameter)
The first 3 methods are helper methods to be used inside the class
- _validate_is_hand(cls, hand: Hand) -> None: As the name implies., verifies that the hand parameter is an instance of Hand, raises TypeError otherwise
      
- _validate_two_cards(cls, hand: Hand) -> None: raises ValueError if the hand does not contain exactly 2 cards

- _validate_two_or_more_cards(cls, hand: Hand) -> None: raises ValueError if the hand contains less than 2 cards

- blackjack(cls, hand: Hand) -> bool: verifies that the received hand is a blackjack. A blackjack is a hand of two cards: an "A" and either a "10", "J", "Q" or "K". Suits are irrelevant. Uses validate_is_hand and _validate_two_cards

- can_double(cls, hand: Hand, valid_doubles: list=[]) -> bool: Some variants of blackjack require that the hand be a certain value to decide if the player can double (eg. 9, 10, 11). Receives the hand to evaluate and an optional list with valid double values. If the list is empty, can_double returns True (if there are exactly 2 cards), if the list is not empty, can_double checks if the value of the hand is in the valid_doubles list and returns True or False accordingly. Raises ValueError if valid_doubles is not a list. All the values in list must be integers, otherwise it raises ValueError. Uses validate_is_hand and _validate_two_cards

- can_split(cls, hand: Hand) -> bool: Receives the hand to evaluate. Returns True if the cards are of the same rank (pair). For blackjack, "10", "J", "Q" or "K", are considered the same rank (eg. a hand with a "10" and "J" is considered a pair). Return False otherwise. Suits are irrelevant. Uses validate_is_hand and _validate_two_cards

- soft(cls, hand: Hand) -> bool: Receives the hand to evaluate. Returns True if the hand is "soft". A hand is soft if it contains an "A", the "A" is counted as 11 and the hand does not bust. Again, suits are irrelevant. By this definition, a blackjack is soft. If the hand contains more than one "A" only one of them can be considered an 11 and, if the hand does not bust, it is also soft. Returns True or False accordingly. Uses validate_is_hand and _validate_two_or_more_cards

- value(cls, hand: Hand) -> int: Returns the value (sum of ranks) of the hand. An "A" can have the values of 1 or 11. If a hand has an "A", it is first counted as 11, if the value is over 21, then we consider the "A" as 1 and return the value. In the case of having more than one "A", one of the "A" will be first considered an 11 and then a 1 if the value of the hand is over 21. Uses validate_is_hand and _validate_two_or_more_cards

- bust(cls, hand: Hand) -> bool: uses the value method. if value(hand) returns anything over 21 bust returns True. Otherwise it returns False. Uses validate_is_hand and _validate_two_or_more_cards




# BlackJackStrategy

The purpose of the BlackJackStrategy class is very simple: it receives the player hand and the dealer up card and returns the correct action (stand, hit, double, split, surrender).

It does nothing else: does not manipulate hands, calculate payouts, make a decision, etc.

It is meant to be used by other code, for example the blackjack simulator

No instances of BlackJackStrategy can be created (no __init__ method). The class will only expose class methods.

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

### Variations
When the player hand has more that 2 cards and the strategy table indicates double or surrender return hit instead.



# RoundOutcome
- RoundOutcome is a class that inherits from Enum.
- Its members are the posible outcomes of a round of blackjack:
    BLACKJACK
    WIN
    PUSH
    LOSS
    DOUBLE_LOSS
    DOUBLE_WIN
    HALF_PAY

- RoundOutcome can be used by any ohter class that needs to react to the outcome of a blackjack hand


# TestDeck
- TestDeck exists only to provide a "known" deck (no random order).
- Controlling the order of the cards in TestDeck, allows us to run tests against BlackJackRound
- TestDeck inherits from Deck and will overwrite methods:
* shuffle(): override this method from Deck to do exactlly the opposite as its name implies: not shuffle the deck! I do this so everything else in the Deck class works as originally intended, already documented and tested.
- All cards are consumed exclusively via Deck.draw().
- Allows reordering cards for deterministic testing.

## Methods
All te following methods will arrange the cards in the deck in an order that guarantees the result specified in the name of the method. For example: for deck_for_bj the order of the deck (without suits) will be: A, 8, K, J (player, dealer, player, dealer)
- deck_for_bj
- deck_for_win
- deck_for_loss
- deck_for_push
- deck_for_double_win
- deck_for_double_loss
- deck_for_split
- deck_for_split_AA
- deck_for_dealer_BJ
- deck_for_split_then_double


# BlackJackRound
Represents the state of a round of Blackjack


## Inputs
- deck: receives the working deck. Validates the deck received is an instance of Deck, otherwise it raises TypeError. The deck should not contain jokers, if it does, raises ValueError.

- hits_soft_17: a flag that indicates if the dealer should hit or stand on a soft 17. Raises TypeError if hits_soft_17 is not bool.

## Attributes
- player_hands: a list of dicts representing the player hand(s). the dict contains the actual hand and two flags, "doubled" and "surrendered"

- dealer_hand: an instance of Hand class. 
