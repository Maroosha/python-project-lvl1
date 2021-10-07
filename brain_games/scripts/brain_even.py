"""Script for even-odd game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine
from brain_games.games.evenodd_game import MESSAGE, evenodd


def main():
    """Play even-odd game.

    Returns:
        game engine function.
    """
    return engine(evenodd, MESSAGE)


if __name__ == '__main__':
    main()
