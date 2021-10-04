"""Play an even-odd game with a user."""


import random

message = 'Answer "yes" if the number is even, otherwise answer "no".'


def func():
    """Even-odd game.

    Returns:
        the game question and the correct answer.

    """
    min_val, max_val = 1, 101
    question = random.randint(min_val, max_val)
    if question % 2 == 0:
        corr = 'yes'
    else:
        corr = 'no'
    return question, corr