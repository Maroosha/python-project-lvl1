"""Script for even-odd game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.evenodd import GAME_RULE, get_question_and_answer


def main():
    """Play even-odd game.

    Returns:
        game engine function.
    """
    return run_engine(get_question_and_answer, GAME_RULE)


if __name__ == '__main__':
    main()
