"""Play an even-odd game with a user.

Continue untill there are 3 correct answers in a row or a single failure.

"""


import random

import prompt


message = 'Answer "yes" if the number is even, otherwise answer "no".'


def func():
    """Even-odd game. Play until 3 correct answers in a row or 1 failure.

    Parameters:
        min_val: min value in range of random int selection.
        max_val: max value in range of random int selection.

    Returns:
        congrats :3 or condolences :(

    """
    question = random.randint(0, 100)
    if question % 2 == 0:
        corr = 'yes'
    else:
        corr = 'no'
    return question, corr
