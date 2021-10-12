"""Script for even-odd game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.evenodd_game import MESSAGE, evenodd


def main():
    """Play even-odd game.

    Returns:
        game engine function.
    """
    return run_engine(evenodd, MESSAGE)


if __name__ == '__main__':
    main()
