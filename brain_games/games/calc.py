"""Play Calculator game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'What is the result of the expression?'


def calc_eval_qa():
    """Play Calculator game.

    Returns:
        the game question and the correct answer.

    """
    min_val, max_val = 0, 101
    n1 = random.randint(min_val, max_val)
    n2 = random.randint(min_val, max_val)
    summ = '{0} + {1}'.format(n1, n2)
    diff = '{0} - {1}'.format(n1, n2)
    mult = '{0} * {1}'.format(n1, n2)
    operations = {summ: n1 + n2, diff: n1 - n2, mult: n1 * n2}
    question = random.choice(list(operations.keys()))
    corr = str(operations[question])
    return question, corr