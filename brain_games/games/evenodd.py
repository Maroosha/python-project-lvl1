"""Play an even-odd game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE, MAX_VALUE = 1, 101


def check_parity(number):
    """
    Check if the value is even or odd.

    Parameters:
        number: integer to be checked.

    Returns:
        'yes' if the value is even or 'no' if it is not

    """
    return 'yes' if number % 2 == 0 else 'no'


def evenodd_eval_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Even-odd game.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    question = random.randint(min_value, max_value)
    corr = check_parity(question)
    return question, corr
