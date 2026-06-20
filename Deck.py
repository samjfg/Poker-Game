import random
from dataclasses import dataclass, field

@dataclass(frozen=True)
class _Card:
    """Each object represents a card in the game."""

    rank: str   # "2".."10", "J", "Q", "K", "A"
    suit: str   # "S", "H", "D", "C"

class _Deck:
    """"""

    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = "SHDC"
        self.cards = [_Card(r, s) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n=1):
        return [self.cards.pop() for _ in range(n)]
    

@dataclass
class _Player:
    name: str
    chips: float = 0.0
    hand: list[_Card] = field(default_factory=list)


class Game:
    def __init__(self, num_players: int, buy_in: float, starting_blind: float):
        self.buy_in = buy_in
        self.starting_blind = starting_blind
        self.players = [_Player(name=f"player_{i}", chips=buy_in) for i in range(num_players)]
        self.dealer_index = 0

    def begin_round(self):
        # Does the initial deal and blinds etc.
        deck = _Deck()
        deck.shuffle()
        print(f"The deck is: \n {deck}")
        for _ in range(2):

            for player in self.players_from(self.small_blind_pos):
                player.hand.extend(deck.deal(1))

        self.rotate_dealer()

    @property
    def small_blind_pos(self) -> int:
        return (self.dealer_index + 1) % len(self.players)

    @property
    def big_blind_pos(self) -> int:
        return (self.dealer_index + 2) % len(self.players)

    def rotate_dealer(self):
        self.dealer_index = (self.dealer_index + 1) % len(self.players)

    def players_from(self, start: int) -> list["_Player"]:
        n = len(self.players)
        return [self.players[(start + i) % n] for i in range(n)]
# Need some way to track small and big blind, I guess just change the dealer. How can I make it so it deals in order too?

if __name__ == "__main__":
    test_game = Game(num_players=4, buy_in = 200, starting_blind = 5)
    test_game.begin_round()

    print(f"Dealer pos: {test_game.dealer_index}")
    print(test_game.players)

    for player in test_game.players:
        print(player.name)
        print(player.chips)
        print(player.hand)

    test_game.begin_round()
    print(f"Dealer pos: {test_game.dealer_index}")
    