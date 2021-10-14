"""Script for Greatest Common Divisor game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.gcd import GAME_RULE, gcd_evaluate_qa


def main():
    """Play gcd game.

    Returns:
        game engine function.
    """
    return run_engine(gcd_evaluate_qa, GAME_RULE)


if __name__ == '__main__':
    main()
