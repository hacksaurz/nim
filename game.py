from random import randint


class Bot():
    def move(self, state):
        raise NotImplementedError


class Random(Bot):
    def move(self, state):
        if any(state):
            pile_index = randint(0, len(state) - 1)
            pile_size = state[pile_index]
            if pile_size >= 1:
                state[pile_index] -= randint(1, pile_size)
                return state
            else:
                return self.move(state)
        else:
            raise ValueError('No stones to take')


class Perfect(Bot):
    pass


class AI(Bot):
    pass


class Game():
    def __init__(self):
        self.perfect = Perfect()
        self.random = Random()
        self.ai = AI()

    def new_game(self, min, max, piles):
        return [randint(min, max) for _ in range(piles)]
