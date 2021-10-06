"""Script for Progression game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine


def main():
    """Play Progression game.

    Returns:
        game engine function.
    """
    return engine('brain-progression')


if __name__ == '__main__':
    main()
