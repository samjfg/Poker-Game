import random
from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    """Each object represents a card in the game."""

    rank: str   # "2".."10", "J", "Q", "K", "A"
    suit: str   # "S", "H", "D", "C"

class Deck:
    """"""

    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = "SHDC"
        self.cards = [Card(r, s) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n=1):
        return [self.cards.pop() for _ in range(n)]
    

class Player:
    def __init__(self, hand: list[Card], chips):
        self.hand = hand
        self.chips = chips


class chips:
    def __init__(self):
        self.chips = chips???
        self.pot = pot???...

    