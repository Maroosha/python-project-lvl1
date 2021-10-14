"""Script for Progression game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.progression import GAME_RULE, progression_evaluate_qa


def main():
    """Play Progression game.

    Returns:
        game engine function.
    """
    return run_engine(progression_evaluate_qa, GAME_RULE)


if __name__ == '__main__':
    main()
