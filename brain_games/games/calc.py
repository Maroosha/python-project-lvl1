"""Play Calculator game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'What is the result of the expression?'
MIN_VALUE, MAX_VALUE = 0, 101


def calc_eval_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Play Calculator game.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    n1 = random.randint(min_value, max_value)
    n2 = random.randint(min_value, max_value)
    summ = '{0} + {1}'.format(n1, n2)
    diff = '{0} - {1}'.format(n1, n2)
    mult = '{0} * {1}'.format(n1, n2)
    operations = {summ: n1 + n2, diff: n1 - n2, mult: n1 * n2}
    question = random.choice(list(operations.keys()))
    corr = str(operations[question])
    return question, corr
