"""Play an even-odd game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE, MAX_VALUE = 1, 101


def check_parity(number):
    """
    Check if the value is even or odd.

    Parameters:
        number: integer to be checked.

    Returns:
        'yes' if the value is even or 'no' if it is not

    """
    return 'yes' if number % 2 == 0 else 'no'


def get_question_and_answer():
    """Evaluate the Q&A for the Even-Odd game.

    Returns:
        the game question and the correct answer.

    """
    question = random.randint(MIN_VALUE, MAX_VALUE)
    correct_answer = check_parity(question)
    return question, correct_answer
