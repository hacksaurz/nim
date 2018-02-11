"""
This module will represent the sate of a game of Nim.
"""
from random import randint

from .bots.bot import Bot
from .exceptions import NimException


class Nim:
    """
    Represent the state of a game of Nim.

    Create a default game, i.e.:
        3 piles
        Random number of stones per pile, with a min of 1 and a max of 20
        Players can take as many stones as they want from a pile
        2 human players (no bots)
    >>> Nim()

    Create a game with a specific state, have 2 bots fight with different
    strategies and they can only take a maximum of 5 stones per turn.
    >>> Nim(state=[4, 9, 7, 13, 6],
            bots=[BotRandom(), BotPerfect()],
            max_stones_one_take=5)

    Create a random game of a specific size with one bot.
    >>> Nim(size=4, bots=[BotRandom()])

    If you pass in a state and a size, the state will take priority. So calling
    >>> Nim(state=[5, 9, 6], size=7)

    will be the same as calling
    >>> Nim(state=[5, 9, 6])

    Similarly, state will take precedence over min_stones_per_pile and
    max_stones_per_pile as those are also used to generate a new random game.
    """
    def __init__(self, size=3, state=None, bots=None, max_stones_one_take=0,
                 min_stones_per_pile=1, max_stones_per_pile=20):
        self.bots = bots
        self.max_stones_one_take = max_stones_one_take
        self.min_stones_per_pile = min_stones_per_pile
        self.max_stones_per_pile = max_stones_per_pile
        if state:
            self.state = state
        else:
            self.state = self.generate_game(size)

    def __repr__(self):
        return ("Nim(size={}, state={}, bots={}, max_stones_one_take={}, "
                "min_stones_per_pile={}, max_stones_per_pile={})"
                .format(self.size, self.state, self.bots,
                        self.max_stones_one_take, self.min_stones_per_pile,
                        self.max_stones_per_pile))

    @property
    def max_stones_one_take(self):
        # If the game has no restrictions on how many stones a player can take
        # from a pile, return the maximum number of stones in the piles to
        # simulate being able to take as many as on wants.
        if self._max_stones_one_take == 0:
            return max(self.state)
        return self._max_stones_one_take

    @max_stones_one_take.setter
    def max_stones_one_take(self, value):
        if not isinstance(value, int):
            raise NimException(
                "max_stones_one_take must be an int: {}"
                .format(value)
            )
        if value < 0:
            raise NimException(
                "max_stones_one_take must be a positive integer "
                "(or 0 for no limit): {}"
                .format(value)
            )
        self._max_stones_one_take = value

    @property
    def min_stones_per_pile(self):
        return self._min_stones_per_pile

    @min_stones_per_pile.setter
    def min_stones_per_pile(self, value):
        if not isinstance(value, int):
            raise NimException(
                "min_stones_per_pile must be an int: {}"
                .format(value)
            )
        if value < 1:
            raise NimException(
                "min_stones_per_pile must be a positive integer: {}"
                .format(value)
            )
        self._min_stones_per_pile = value

    @property
    def max_stones_per_pile(self):
        return self._max_stones_per_pile

    @max_stones_per_pile.setter
    def max_stones_per_pile(self, value):
        if not isinstance(value, int):
            raise NimException(
                "max_stones_per_pile must be an int: {}"
                .format(value)
            )
        # We could interpret 0 as infinity, but for now let's set an actual max
        if value < 1:
            raise NimException(
                "max_stones_per_pile must be a positive integer: {}"
                .format(value)
            )
        self._max_stones_per_pile = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        try:
            value_int = [int(x) for x in value]
        except (TypeError, ValueError):
            raise NimException(
                "The state needs to be a list of integers: {}"
                .format(value)
            )
        if any(x < 0 for x in value_int):
            raise NimException(
                "Can't have piles with negative amounts of stones: {}"
                .format(value_int)
            )
        self._state = value_int

    @property
    def size(self):
        return len(self.state)

    @property
    def bots(self):
        return self._bots

    @bots.setter
    def bots(self, value):
        if value is None:
            value = []
        try:
            iter(value)
        except TypeError:
            raise NimException(
                "The bots argument must be a list of Bot: {}"
                .format(value)
            )
        if not 0 <= len(value) <= 2:
            raise NimException(
                "There can only be between 0 and 2 bots: {}"
                .format(value)
            )
        if not all(isinstance(bot, Bot) for bot in value):
            raise NimException(
                "Bots must inherit from the Bot class: {}"
                .format(value)
            )
        self._bots = value

    def generate_game(self, size):
        """
        Generate a new random state for the game.
        """
        if self.min_stones_per_pile > self.max_stones_per_pile:
            raise NimException(
                "Can't generate a game because min_stones_per_pile if larger "
                "then max_stones_per_pile: {} > {}"
                .format(self.min_stones_per_pile, self.max_stones_per_pile)
            )
        return [randint(self.min_stones_per_pile, self.max_stones_per_pile)
                for _ in range(size)]
