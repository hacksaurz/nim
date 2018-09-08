from operator import itemgetter
from typing import Dict, List

from random import choice, randint

from nim.exceptions import NimException

ABS_MIN_STONES_PER_PILE: int = 1
ABS_MAX_STONES_PER_PILE: int = 50
ABS_MIN_NUM_PILES: int = 1
ABS_MAX_NUM_PILES: int = 50

DEFAULT_MIN_STONES_PER_PILE: int = 5
DEFAULT_MAX_STONES_PER_PILE: int = 20
DEFAULT_NUM_PILES: int = 3


class Bot():
    subclasses: List = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Bot.subclasses.append(cls)

    def nonzero_pile_indexes(self, state: List[int]) -> List[int]:
        return [i for i, nb_stones in enumerate(state) if nb_stones >= 1]

    def move(self, state: List[int]) -> Dict[str, int]:
        if not self.nonzero_pile_indexes(state):
            raise NimException(f'No valid moves on state: {state}')
        return self.move_strategy(state)

    def move_strategy(self, state: List[int]) -> Dict[str, int]:
        """
        Need to be implemented when subclassing.
        """
        raise NotImplementedError


class Random(Bot):
    """
    Bot that always chooses a random number of stones from a random pile
    """
    def move_strategy(self, state: List[int]) -> Dict[str, int]:
        pile_index: int = choice(self.nonzero_pile_indexes(state))
        stones: int = randint(1, state[pile_index])
        return {'pile': pile_index, 'stones': stones}


class Perfect(Bot):
    """
    Hunter's bot :)
    Temporary strategy until implemented
    """
    def move_strategy(self, state: List[int]) -> Dict[str, int]:
        pile_index: int = choice(self.nonzero_pile_indexes(state))
        return {'pile': pile_index, 'stones': 1}


class AI(Bot):
    """
    Temporary strategy until implemented
    """
    def move_strategy(self, state: List[int]) -> Dict[str, int]:
        pile_index: int = choice(self.nonzero_pile_indexes(state))
        return {'pile': pile_index, 'stones': 1}


class Greedy(Bot):
    """
    Bot that always takes as many stones as possible
    """
    def move_strategy(self, state: List[int]) -> Dict[str, int]:
        # pile_index: int, stones: int
        pile_index, stones = max(enumerate(state), key=itemgetter(1))
        return {'pile': pile_index, 'stones': stones}


class Garbage(Bot):
    """
    I always take one stone from the first available pile!
    Derp! :D
    """
    def move_strategy(self, state: List[int]) -> Dict[str, int]:
        pile_index: int = self.nonzero_pile_indexes(state)[0]
        return {'pile': pile_index, 'stones': 1}


class Chaos(Bot):
    """
    Bot that chooses a random other bot strategy to make a move
    """
    def move_strategy(self, state: List[int]) -> Dict[str, int]:
        """
        Takes the state of the game and returns the result of another bot's
        move
        """
        not_chaos_bot: List[type] = [bot for bot in Bot.subclasses
                                     if bot != Chaos]
        chosen_bot: Bot = choice(not_chaos_bot)()
        return chosen_bot.move_strategy(state)


class Nim():
    def __init__(self):
        self.perfect: Bot = Perfect()
        self.random: Bot = Random()
        self.ai: Bot = AI()
        self.garbage: Bot = Garbage()
        self.greedy: Bot = Greedy()
        self.chaos: Bot = Chaos()

    @staticmethod
    def new_game(min_stones_per_pile: int = DEFAULT_MIN_STONES_PER_PILE,
                 max_stones_per_pile: int = DEFAULT_MAX_STONES_PER_PILE,
                 num_piles: int = DEFAULT_NUM_PILES) -> List[int]:
        """
        Logic of new game dealt with here. Uses min_stones_per_pile,
        max_stones_per_pile & num_piles to return a list of piles
        """
        if not all(isinstance(x, int) and
                   ABS_MIN_STONES_PER_PILE <= x <= ABS_MAX_STONES_PER_PILE
                   for x in (min_stones_per_pile, max_stones_per_pile)):
            raise NimException(
                f"Please use integers between {ABS_MIN_STONES_PER_PILE} and "
                "{ABS_MAX_STONES_PER_PILE} for the number of stones"
            )
        elif not (isinstance(num_piles, int) and
                  ABS_MIN_NUM_PILES <= num_piles <= ABS_MAX_NUM_PILES):
            raise NimException(
                f"Please use an integer between {ABS_MIN_NUM_PILES} and "
                "{ABS_MAX_NUM_PILES} for the number of piles"
            )
        elif min_stones_per_pile > max_stones_per_pile:
            raise NimException(
                f"min_stones_per_pile ({min_stones_per_pile}) can't be "
                "greater than max_stones_per_pile ({max_stones_per_pile})"
            )
        return [randint(min_stones_per_pile, max_stones_per_pile)
                for _ in range(num_piles)]

    def update(self, state: List[int], move: Dict[str, int]) -> None:
        if not self.is_valid_move(state, move):
            raise NimException(f"{move} not a valid move on {state} state")
        state[move['pile']] -= move['stones']

    def is_valid_move(self, state: List[int], move: Dict[str, int]) -> bool:
        try:
            state[move['pile']]
        except IndexError:
            return False
        return 1 <= move['stones'] <= state[move['pile']]
