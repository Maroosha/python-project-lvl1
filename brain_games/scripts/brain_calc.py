"""Script for Calculator game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.calc_game import MESSAGE, calc


def main():
    """Play Calculator game.

    Returns:
        game engine function.
    """
    return run_engine(calc, MESSAGE)


if __name__ == '__main__':
    main()
