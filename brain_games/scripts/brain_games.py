"""Welcome a user."""

# !/usr/bin/env python3

from brain_games.cli import welcome_user


def main():
    """Welcome the user."""
    print('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == '__main__':
    main()
