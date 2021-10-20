"""Play an even-odd game with a user."""

# !/usr/bin/env python3


import random
import types

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE, MAX_VALUE = 1, 101
PARITY_CHECK = types.MappingProxyType({True: 'yes', False: 'no'})


def is_even(number):
    """
    Check if the value is even or odd.

    Parameters:
        number: integer to be checked.

    Returns:
        True if the value is even or False if it is odd.
    """
    return number % 2 == 0


def get_question_and_answer():
    """Evaluate the Q&A for the Even-Odd game.

    Returns:
        the game question and the correct answer.
    """
    question = random.randint(MIN_VALUE, MAX_VALUE)
    correct_answer = PARITY_CHECK[is_even(question)]
    return question, correct_answer
