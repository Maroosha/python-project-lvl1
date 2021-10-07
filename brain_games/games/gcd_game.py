"""Play the Greatest Common Divisor game with a user."""

# !/usr/bin/env python3


import random

MESSAGE = 'Find the greatest common divisor of given numbers.'


def gcd():
    """Play the greatest common divisor game.

       Corr is evaluated using Euclidean algo for gcd.

    Returns:
        the game question and the correct answer.

    """
    min_val, max_val = 1, 101
    n1 = random.randint(min_val, max_val)
    n2 = random.randint(min_val, max_val)
    question = '{0} {1}'.format(n1, n2)
    num1, num2 = max(n1, n2), min(n1, n2)
    remainder = num1 % num2
    while remainder != 0:
        num1, num2 = num2, remainder
        remainder = num1 % num2
    corr = str(num2)
    return question, corr
