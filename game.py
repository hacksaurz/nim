from random import randint

from exceptions import NimException


class Bot():
    def move(self, state):
        raise NotImplementedError


class Random(Bot):
    """
    Cory's bot :)
    """
    pass


class Perfect(Bot):
    """
    Hunter's bot :)
    """
    pass


class AI(Bot):
    pass


class Garbage(Bot):
    """
    I always take one stone from the first available pile!
    Derp! :D
    """
    def move(self, state):
        for i, pile in enumerate(state):
            if pile >= 1:
                return {'pile': i, 'stones': 1}
        raise NimException('No stones to take')


class Nim():
    def __init__(self):
        self.perfect = Perfect()
        self.random = Random()
        self.ai = AI()
        self.garbage = Garbage()

    def new_game(self, min, max, piles):
        return [randint(min, max) for _ in range(piles)]

    def update(self, state, move):
        if not self.is_valid_move(state, move):
            raise NimException(f"{move} not a valid move on {state} state")
        state[move['pile']] -= move['stones']

    def is_valid_move(self, state, move):
        try:
            state[move['pile']]
        except IndexError:
            return False
        return 1 <= move['stones'] <= state[move['pile']]
