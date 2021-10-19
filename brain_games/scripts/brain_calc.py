"""Script for Calculator game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.calc import GAME_RULE, get_question_and_answer


def main():
    """Play Calculator game.

    Returns:
        game engine function.
    """
    return run_engine(get_question_and_answer, GAME_RULE)


if __name__ == '__main__':
    main()
