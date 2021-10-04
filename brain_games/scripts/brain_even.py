"""Script for even-odd game."""

# !/usr/bin/env python3


from brain_games.game_engine import welcome_user, engine


def main():
    """Play even-odd game.

    Returns:
        congrats :3 or condolences :(
    """
    return engine('brain-even')


if __name__ == '__main__':
    main()
