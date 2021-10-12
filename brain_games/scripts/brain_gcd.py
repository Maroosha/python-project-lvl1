"""Script for Greatest Common Divisor game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.gcd_game import MESSAGE, gcd


def main():
    """Play gcd game.

    Returns:
        game engine function.
    """
    return run_engine(gcd, MESSAGE)


if __name__ == '__main__':
    main()
