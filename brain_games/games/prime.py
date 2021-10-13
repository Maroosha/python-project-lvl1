"""Play the prime-or-not-prime game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_VALUE, MAX_VALUE = 1, 101


def prime_eval_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Play the prime-or-not-prime game.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    num = random.randint(min_value, max_value)
    question = '{0}'.format(num)
    if num == 1:
        corr = 'yes'
    elif num == 2:
        corr = 'yes'
    for elem in range(2, num):
        if num % elem == 0:
            corr = 'no'
            break
        else:
            corr = 'yes'
    return question, corr
