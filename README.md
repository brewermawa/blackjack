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

Represents a single complete round of Blackjack, from the initial deal until a terminal outcome is reached.

## Scope

- Deals only with the current round. Does not care about bet size or how many cards are in the shoe (the calling class is in charge of the shoe/deck and bets).

- BlackJackRound is responsible for resolving all hands derived from a single initial player hand, including splits (only 1 split allowed in this version).

- Returns the result to the calling function/method

- Uses BlackJackEval and BlackjackStrategy methods to control the flow of the game


## Inputs
- deck: receives the working deck. Validates the deck received is an instance of Deck, otherwise it raises TypeError. The deck should not contain jokers, if it does, raises ValueError.

- hits_soft_17: a flag that indicates if the dealer should hit or stand on a soft 17. Raises TypeError if hits_soft_17 is not bool.

## Attributes
- player_hand: an instance of Hand class. Contains the player cards. When the BlackJackRound class is initialized, player_hand is created but no cards are added
- dealer_hand: an instance of Hand class. Contains the dealer cards. When the BlackJackRound class is initialized, dealer_hand is created but no cards are added
- `player_doubled`: a flag that indicates whether the player executed a `DOUBLE` action in this round (per `BlackJackStrategy`).


## Methods
- play():
* Handles card dealing. Uses BlackJackEval and BlackJackStrategy to control the flow of the round

* Returns the round result: This will be a list with a length equal to how many hands the players had. In  this initial version split will not be implemented. The list returned will be of length 1

* The possible items returned in the results list are members of Class RoundOutcome


## Invariants

- All cards used during the round must be drawn from the provided deck.

- A hand can only have exactly one outcome. Once the outcome is reached, no more cards should be dealt to that hand

- A round always terminates once all player hands and the dealer hand reach a terminal state.

```markdown

# Blackjack Round (`play()`) – High Level Design (Current Scope)

> Scope note:  
> At this stage, **split is intentionally excluded** to reduce complexity.  
> The round supports a single player hand and a single dealer hand.

---

## Round Flow

```
initial_deal
→ blackjack check
→ surrender check
→ player_turn
→ dealer_turn
→ compare_hands
→ list[RoundOutcome]
```

`play()` always returns a **list of `RoundOutcome`**, even if there is only one outcome.

---

## Early Termination Rules

Some stages may end the round immediately.

### Terminator stages
- `blackjack`
- `surrender`

If any of these stages returns an outcome:

- the outcome is appended to the outcomes list
- `play()` returns immediately

If they return `None`, execution continues.

---

## Hand Model

### Hand
- Stores **only cards**
- Does not store totals or flags

### No state is persisted in `Hand`
- no `is_bust`
- no `total`
- no `soft`
- no `blackjack`

All evaluations are computed dynamically.

---

## BlackJackEval Responsibilities

`BlackJackEval` is responsible for all rule evaluation:

- `total(hand)`
- `is_soft(hand)`
- `is_bust(hand)`
- `is_blackjack(hand)`

Evaluation is deterministic and stateless.

---

## BlackJackStrategy

`BlackJackStrategy` decides the player action.

### Action enum

```python
HIT
STAND
DOUBLE
SPLIT
SURRENDER
```

---

## Player Turn

### Preconditions

- Blackjack already resolved
- Surrender already resolved
- Split is not supported


### Valid actions in this phase

- HIT
- STAND
- DOUBLE

If the strategy returns `SPLIT` or `SURRENDER` here, it is considered an error.


## Player Turn Contract

### Inputs
- `player_hand`
- `dealer_up_card` (`dealer_hand[0]`)
- `BlackJackStrategy`
- `deck`

### Side Effects
- Draws cards from the deck
- Modifies `player_hand`

### Output
- Returns nothing
- Leaves the hand in a terminal state

### Terminal states
- STAND
- BUST


## Player Turn Pseudocode

```text
while True:

    action = BlackJackStrategy.strategy(player_hand, dealer_up_card)

    if action == HIT:
        draw 1 card from deck
        add card to player_hand

        if BlackJackEval.is_bust(player_hand):
            break
        else:
            continue

    elif action == DOUBLE:
        set player_doubled to True
        draw 1 card from deck
        add card to player_hand
        break

    elif action == STAND:
        break

    else:
        error (invalid action for player_turn)
```

## Dealer Turn

Dealer turn only executes if player_hand is not bust

### Preconditions

- Blackjack already resolved
- Surrender already resolved
- Player turn already resolved
- Split is not supported

## Dealer Turn Contract

### Inputs
- `dealer_hand`
- `deck`
- `BlackJackEval`
- `hits_soft_17`


### Side Effects
- Draws cards from the deck
- Modifies `dealer_hand`

### Output
- Returns nothing
- Leaves dealer_hand in a terminal state

### Terminal states
- STAND
- BUST

## Dealer turn algorithm

```text
1. Dealer turn
    1. while (
            dealer hand value < 17
            or (dealer hand is soft 17 and hits_soft_17 is True)
        )
        1. draw one card and add it to dealer hand
        2. If bust, exit loop
        3. If not bust, continue loop
 ```


## Compare hands

After the player and dealer hands are in a terminal state, compares boths and returns a result

### Preconditions

- Blackjack already resolved
- Surrender already resolved
- Player turn already resolved
- Dealer turn already resolved

## Compare hands Contract


### Inputs
- `player_hand`
- `dealer_hand`
- `BlackJackEval`


### Side Effects
. No side effects

### Output
- Returns list[RoundOutcome]


## Compare hands algorithm

```text
1. If player_hand is bust:
       if player_doubled:
           return [DOUBLE_LOSS]
       else:
           return [LOSS]

2. If dealer_hand is bust:
       if player_doubled:
           return [DOUBLE_WIN]
       else:
           return [WIN]

3. If value(player_hand) == value(dealer_hand):
       return [PUSH]

4. If value(player_hand) > value(dealer_hand):
       if player_doubled:
           return [DOUBLE_WIN]
       else:
           return [WIN]

5. Else:
       if player_doubled:
           return [DOUBLE_LOSS]
       else:
           return [LOSS]

```

## Split
BlackJackRound v2 – Split MVP

Rules:
- Splits are only allowed on two cards of the same value (10, J, Q and K are considered the same value)
- For this version only splitting one time is allowed
- After the split, the 2 hands created are treated as regular hands.
- After the split 2 hands exist: hand 1 and hand 2. hand 1 must be resolved according to BlackJackStrategy before dealing the second card to hand2
- When splitting aces only an additional card is dealt per hand.
- When splitting, the second card of the original hand (hand[1]) is moved to a new hand. Because the card vallues are the same in the original hand, its really irrelevant which card is moved to the new hand but we must define it for this simulation
- A blackjack after splitting (10s or As) is considered a normal win (no extra pay for blackjack, 3:2, 6:5, etc.)
- No double after split allowed in this version
- As with any other player hand, dealer play is not affected
- ValueError if BlackJackStrategy returns DOUBLE or SURRENDER
- Each hand has a separate result, play will return a list with the outcome of both hands
- If a split occurs, play() returns a list of length 2; otherwise length 1.
- BlackJackStrategy is the only decision maker
- Surrender is not available after split
- Each hand has independent state (e.g., doubled flag, outcome).

## v3.0 (DAS and SURRENDRER -> HIT after split)
- DAS (Double After Split): after a split, if Strategy returns DOUBLE for a specific split hand, deal exactly one additional card to that hand and end that hand immediately. The outcome for that hand must be evaluated as a double (DOUBLE_WIN, DOUBLE_LOSS, or PUSH).
- Surrender fallback after split: after a split, if Strategy returns SURRENDER, treat it as HIT (draw one card) and continue play normally. This mapping applies every time SURRENDER is returned in a split-hand context.

## v4.0 Allow resplits
1) Maximum Splits
The player may perform up to 3 splits, resulting in a maximum of 4 player hands.
Any attempt to split beyond this limit must raise NotImplementedError.

2) Resplit Policy
Resplitting aces is not allowed.
If Strategy returns SPLIT for a hand that originated from split aces, the engine must raise NotImplementedError.

3) Per-Hand Split Limit
Each individual hand may be split at most once.
A split operation creates exactly one additional hand.

4) Generalized Variant A (Multi-Hand)
Player hands are resolved sequentially in creation order.
For each hand:
The second card is dealt (if needed).
The hand is fully resolved before the next hand receives its second card.
This ordering applies across all split levels.

5) Split Aces Constraint (Reaffirmed for Multi-Split)
When aces are split:
Each resulting hand receives exactly one additional card.
Each hand automatically stands.
This rule applies regardless of how many total hands exist due to prior splits.

6) Dealer Resolution with Multi-Hands
The dealer plays exactly once, after all player hands (including all split hands) have been fully resolved.
All player hands are compared against the same final dealer hand.

7) Outcome Ordering
play() returns a list of outcomes whose length equals the final number of player hands.
Outcomes are returned in the same order as the corresponding player hands were created.

# Fixed Deck
FixedDeck is a helper class used only for testing purposes.

Its goal is to return a deck with the first N cards fixed, for example:

def deck_for_bj(self):
    self._program_ranks_top(["A", "8", "K", "J"])

Where the "A" and "K" will be dealt to the player and "8" and "J" to the dealer
