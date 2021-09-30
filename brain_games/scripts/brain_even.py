"""Script for even-odd game."""

# !/usr/bin/env python3

from brain_games.evenodd_game import oe_func


def main():
    """Play even-odd game.

    Returns:
        greetings.
    """
    print('Welcome to the Brain Games!')
    return oe_func(min_val=1, max_val=50)


if __name__ == '__main__':
    main()
