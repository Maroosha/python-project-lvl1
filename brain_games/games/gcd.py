"""Play the Greatest Common Divisor game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'
MIN_VALUE, MAX_VALUE = 1, 101


def gcd_eval_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Play the greatest common divisor game.

       Corr is evaluated using Euclidean algo for gcd.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    n1 = random.randint(min_value, max_value)
    n2 = random.randint(min_value, max_value)
    question = '{0} {1}'.format(n1, n2)
    num1, num2 = max(n1, n2), min(n1, n2)
    remainder = num1 % num2
    while remainder != 0:
        num1, num2 = num2, remainder
        remainder = num1 % num2
    corr = str(num2)
    return question, corr
