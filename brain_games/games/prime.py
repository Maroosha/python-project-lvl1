"""Play the Prime-or-Not game with a user."""

# !/usr/bin/env python3


import random
import types

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_VALUE, MAX_VALUE = 1, 101
PRIMALITY_CHECK = types.MappingProxyType({True: 'yes', False: 'no'})


def is_prime(number):
    """
    Check whether a value is prime or not.

    Parameters:
        number: integer to be checked.

    Returns:
        True if the value is prime; False if it is not.
    """
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def get_question_and_answer():
    """Evaluate the Q&A for the Prime-or-Not game.

    Returns:
        the game question and the correct answer.
    """
    number = random.randint(MIN_VALUE, MAX_VALUE)
    question = '{0}'.format(number)
    correct_answer = PRIMALITY_CHECK[is_prime(number)]
    return question, correct_answer
