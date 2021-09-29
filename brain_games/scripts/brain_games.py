"""Welcome a user."""

# !/usr/bin/env python3

import logging

from brain_games.cli import welcome_user


def main():
    """Welcome the user."""
    log = logging.getLogger()
    log.info('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == '__main__':
    main()
