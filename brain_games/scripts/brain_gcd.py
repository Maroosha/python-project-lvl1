"""Script for Greatest Common Divisor game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine


def main():
    """Play gcd game.

    Returns:
        game engine function.
    """
    return engine('brain-gcd')


if __name__ == '__main__':
    main()
