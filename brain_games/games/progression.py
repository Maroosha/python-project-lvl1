"""Play the Guess-the-Progression-Element game with a user."""

# !/usr/bin/env python3


import random
import types

GAME_RULE = 'What number is missing in the progression?'
RANDOM_RANGE = types.MappingProxyType({     # make a dictionary immutable
    'min_value': 1,
    'max_value': 101,
    'd_min': 2,
    'd_max': 10,
    'progression_len_min': 5,
    'progression_len_max': 10,
})


def create_sequence(random_range):
    """
    Create an arithmetic sequence.

    Parameters:
        random_range: dictionary of min and max values for random selection.

    Returns:
        arithmetic sequence as a list of integers.

    """
    a1 = random.randint(random_range['min_value'], random_range['max_value'])
    # sticking to delta instead of d notation to satisfy WPS111 and WPS120 errs
    delta = random.randint(random_range['d_min'], random_range['d_max'])
    len_progression = random.randint(
        random_range['progression_len_min'],
        random_range['progression_len_max'],
    )
    progressn = [a1]
    for element in range(1, len_progression):
        progressn.append(progressn[element - 1] + delta)
    return progressn


def int_list_to_str_list(int_list):
    """
    Convert a list of integers into a list of strings.

    Parameters:
        int_list: list of integers.

    Returns:
        list of strings.
    """
    return [str(element) for element in int_list]


def get_question_and_answer():
    """Evaluate the Q&A for the Guess-the-Progression-Element game.

    Returns:
        the game question and the correct answer.

    """
    progressn = create_sequence(RANDOM_RANGE)
    str_progressn = int_list_to_str_list(progressn)
    empty = random.choice(range(len(progressn)))
    correct_answer = str(progressn[empty])
    str_progressn[empty] = '..'
    question = ' '.join(str_progressn)
    return question, correct_answer
