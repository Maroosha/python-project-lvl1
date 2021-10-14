"""Script for even-odd game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.evenodd import GAME_RULE, evenodd_evaluate_qa


def main():
    """Play even-odd game.

    Returns:
        game engine function.
    """
    return run_engine(evenodd_evaluate_qa, GAME_RULE)


if __name__ == '__main__':
    main()
