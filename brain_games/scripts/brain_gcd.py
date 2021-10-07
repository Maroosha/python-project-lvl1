"""Script for Greatest Common Divisor game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine
from brain_games.games.gcd_game import MESSAGE, gcd


def main():
    """Play gcd game.

    Returns:
        game engine function.
    """
    return engine(gcd, MESSAGE)


if __name__ == '__main__':
    main()
