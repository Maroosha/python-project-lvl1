"""Script for prime-or-not-prime game."""

# !/usr/bin/env python3


from brain_games.game_engine import engine


def main():
    """Play prime-or-not-prime game.

    Returns:
        game engine function.
    """
    return engine('brain-prime')


if __name__ == '__main__':
    main()
