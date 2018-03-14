from operator import itemgetter

from random import choice, randint

from nim.exceptions import NimException

NUM_LIMIT = 50
DEFAULT_GAME = {'min': 5, 'max': 15, 'piles': 4}


class Bot():
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Bot.subclasses.append(cls)

    def nonzero_pile_indexes(self, state):
        return [i for i, nb_stones in enumerate(state) if nb_stones >= 1]

    def move(self, state):
        if not self.nonzero_pile_indexes(state):
            raise NimException(f'No valid moves on state: {state}')
        return self.move_strategy(state)


class Random(Bot):
    """
    Bot that always chooses a random number of stones from a random pile
    """
    def move_strategy(self, state):
        pile_index = choice(self.nonzero_pile_indexes(state))
        stones = randint(1, state[pile_index])
        return {'pile': pile_index, 'stones': stones}


class Perfect(Bot):
    """
    Hunter's bot :)
    Temporary strategy until implemented
    """
    def move_strategy(self, state):
        pile_index = choice(self.nonzero_pile_indexes(state))
        return {'pile': pile_index, 'stones': 1}


class AI(Bot):
    """
    Temporary strategy until implemented
    """
    def move_strategy(self, state):
        pile_index = choice(self.nonzero_pile_indexes(state))
        return {'pile': pile_index, 'stones': 1}


class Greedy(Bot):
    """
    Bot that always takes as many stones as possible
    """
    def move_strategy(self, state):
        pile_index, stones = max(enumerate(state), key=itemgetter(1))
        return {'pile': pile_index, 'stones': stones}


class Garbage(Bot):
    """
    I always take one stone from the first available pile!
    Derp! :D
    """
    def move_strategy(self, state):
        pile_index = self.nonzero_pile_indexes(state)[0]
        return {'pile': pile_index, 'stones': 1}


class Chaos(Bot):
    """
    Bot that chooses a random other bot strategy to make a move
    """
    def move_strategy(self, state):
        """
        Takes the state of the game and returns the result of another bot's move
        """
        not_chaos_bot = [bot for bot in Bot.subclasses if bot != Chaos]
        chosen_bot = choice(not_chaos_bot)()
        return chosen_bot.move_strategy(state)


class Nim():
    def __init__(self):
        self.perfect = Perfect()
        self.random = Random()
        self.ai = AI()
        self.garbage = Garbage()
        self.greedy = Greedy()
        self.chaos = Chaos()

    def new_game(self, min, max, piles):
        """
        Logic of new game dealt with here.
        Uses either user-passed JSON or
        default values to fill in params
        """
        if not all(isinstance(x, int) and 1 <= x <= NUM_LIMIT
                   for x in (min, max, piles)):
            raise NimException(
                f"Please use integers between 1 and {NUM_LIMIT}")
        elif min > max:
            raise NimException(
                f"Min({min}) cant be greater than Max({max})")
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
