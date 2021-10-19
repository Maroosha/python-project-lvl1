"""Play the Greatest Common Divisor game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'
MIN_VALUE, MAX_VALUE = 1, 101


def evaluate_gcd(number1, number2):
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


def get_question_and_answer():
    """Evaluate the Q&A for the Greatest Common Divisor game.

    Returns:
        the game question and the correct answer.

    """
    number1 = random.randint(MIN_VALUE, MAX_VALUE)
    number2 = random.randint(MIN_VALUE, MAX_VALUE)
    question = '{0} {1}'.format(number1, number2)
    correct_answer = str(evaluate_gcd(number1, number2))
    return question, correct_answer
