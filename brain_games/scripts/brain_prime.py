"""Script for prime-or-not-prime game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.prime_game import MESSAGE, prime


def main():
    """Play prime-or-not-prime game.

    Returns:
        game engine function.
    """
    return run_engine(prime, MESSAGE)


if __name__ == '__main__':
    main()
