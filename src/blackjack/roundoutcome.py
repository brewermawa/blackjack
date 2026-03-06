from enum import Enum


class RoundOutcome(Enum):
    BLACKJACK = "blackjack"
    WIN = "win"
    PUSH = "push"
    LOSS = "loss" 
    DOUBLE_WIN = "double win"
    DOUBLE_LOSS = "double loss"
    HALF_PAY = "half pay"