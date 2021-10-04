"""Script for Calculator game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine


def main():
    """Play Calculator game.

    Returns:
        game engine function.
    """
    return engine('brain-calc')


if __name__ == '__main__':
    main()
