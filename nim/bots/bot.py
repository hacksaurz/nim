"""
Bots that play Nim.
"""


class Move:
    """
    A move consists of a pile number and an amount of stones to take.
    """
    def __init__(self, pile, stones):
        self.pile = pile
        self.stones = stones


class Bot:
    """
    A bot that plays Nim.
    Basic class to inherit from when defining your own bot.
    """
    STRAT = "Unknown"

    def __repr__(self):
        return "Bot({})".format(self.STRAT)

    def get_next_move(self, game):
        """
        Analyze the game and return your next move.
        To be implemented in subclasses.
        """
        raise NotImplementedError
