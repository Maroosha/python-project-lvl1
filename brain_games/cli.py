"""Ask a user their name. Return greeting."""

# !/usr/bin/env python3

import prompt


def welcome_user():
    """Ask the user their name and return the greeting.

    Returns:
        congrats
    """
    name = prompt.string('May I have your name? ')
    return 'Hello, {0}!'.format(name)
