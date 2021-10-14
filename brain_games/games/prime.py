"""Play the Prime-or-Not game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_VALUE, MAX_VALUE = 1, 101


def check_primality(number):
    """
    Check whether a value is prime or not.

    Parameters:
        number: integer to be checked.

    Returns:
        'yes' if the value is prime; 'no' if it is not.
    """
    for element in range(2, number):
        if number % element == 0:
            return 'no'
    return 'yes'


def prime_evaluate_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Evaluate the Q&A for the Prime-or-Not game.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    number = random.randint(min_value, max_value)
    question = '{0}'.format(number)
    correct_answer = check_primality(number)
    return question, correct_answer
