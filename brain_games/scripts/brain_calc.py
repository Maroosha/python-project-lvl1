"""Script for Calculator game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.calc import GAME_RULE, calc_evaluate_qa


def main():
    """Play Calculator game.

    Returns:
        game engine function.
    """
    return run_engine(calc_evaluate_qa, GAME_RULE)


if __name__ == '__main__':
    main()
