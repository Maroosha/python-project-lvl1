"""Script for prime-or-not-prime game."""

# !/usr/bin/env python3


from brain_games.engine import run_engine
from brain_games.games.prime import GAME_RULE, prime_evaluate_qa


def main():
    """Play prime-or-not-prime game.

    Returns:
        game engine function.
    """
    return run_engine(prime_evaluate_qa, GAME_RULE)


if __name__ == '__main__':
    main()
