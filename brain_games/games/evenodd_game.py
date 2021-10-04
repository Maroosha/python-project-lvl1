"""Play an even-odd game with a user.

Continue untill there are 3 correct answers in a row or a single failure.

"""


import random

message = 'Answer "yes" if the number is even, otherwise answer "no".'


def func():
    """Even-odd game. Play until 3 correct answers in a row or 1 failure.

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
