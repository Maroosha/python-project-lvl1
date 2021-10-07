"""Play the prime-or-not-prime game with a user."""

# !/usr/bin/env python3


import random

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    """Play the prime-or-not-prime game.

    Returns:
        the game question and the correct answer.

    """
    min_val, max_val = 1, 101
    num = random.randint(min_val, max_val)
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
