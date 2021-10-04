"""Script for even-odd game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine


def main():
    """Play even-odd game.

    Returns:
        game engine function.
    """
    return engine('brain-even')


if __name__ == '__main__':
    main()
