"""Play the Greatest Common Divisor game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'
MIN_VALUE, MAX_VALUE = 1, 101


def eval_gcd(number1, number2):
    """
    Evaluate the greatest common divisor via Euclidian algo for gcd.

    Parameters:
        number1: first integer;
        number2: second integer.

    Returns:
        the greatest common divisor.
    """
    value1, value2 = max(number1, number2), min(number1, number2)
    remainder = value1 % value2
    while remainder != 0:
        value1, value2 = value2, remainder
        remainder = value1 % value2
    return value2


def gcd_eval_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Play the greatest common divisor game.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    number1 = random.randint(min_value, max_value)
    number2 = random.randint(min_value, max_value)
    question = '{0} {1}'.format(number1, number2)
    correct_answer = str(eval_gcd(number1, number2))
    return question, correct_answer
