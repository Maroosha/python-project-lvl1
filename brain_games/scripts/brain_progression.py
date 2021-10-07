"""Script for Progression game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine
from brain_games.games.progression_game import MESSAGE, progression


def main():
    """Play Progression game.

    Returns:
        game engine function.
    """
    return engine(progression, MESSAGE)


if __name__ == '__main__':
    main()
