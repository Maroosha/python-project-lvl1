"""Play Progression game with a user."""

# !/usr/bin/env python3


import random

message = 'What number is missing in the progression?'


def func():
    """Play Progression game.

    Returns:
        the game question and the correct answer.

    """
    rand_range = {
        'min_val': 1,
        'max_val': 101,
        'delta_min': 2,
        'delta_max': 10,
        'len_min': 5,
        'len_max': 10,
    }
    start = random.randint(rand_range['min_val'], rand_range['max_val'])
    delta = random.randint(rand_range['delta_min'], rand_range['delta_max'])
    len_progr = random.randint(rand_range['len_min'], rand_range['len_max'])
    progression = [start]
    for elem in range(1, len_progr):
        progression.append(progression[elem - 1] + delta)
    empty = random.choice(range(len_progr))
    corr = str(progression[empty])   # correct answer
    progression = [str(elemt) for elemt in progression]
    progression[empty] = '..'
    question = ' '
    question = question.join(progression)   # question
    return question, corr
