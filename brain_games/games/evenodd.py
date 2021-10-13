"""Play an even-odd game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE, MAX_VALUE = 1, 101


def evenodd_eval_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Even-odd game.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    question = random.randint(min_value, max_value)
    if question % 2 == 0:
        corr = 'yes'
    else:
        corr = 'no'
    return question, corr
