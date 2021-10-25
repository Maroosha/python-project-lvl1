"""Play the Guess-the-Progression-Element game with a user."""

# !/usr/bin/env python3


import random
import types

GAME_RULE = 'What number is missing in the progression?'
RANDOM_RANGE = types.MappingProxyType({     # make a dictionary immutable
    'min_value': 1,
    'max_value': 101,
    'common_difference_min': 2,
    'common_difference_max': 10,
    'number_of_terms_min': 5,
    'number_of_terms_max': 10,
})


def create_arithmetic_progression():
    """
    Create an arithmetic progression.

    Returns:
        arithmetic progression as a list of integers.
    """
    initial_term = random.randint(
        RANDOM_RANGE['min_value'],
        RANDOM_RANGE['max_value'],
    )
    common_difference = random.randint(
        RANDOM_RANGE['common_difference_min'],
        RANDOM_RANGE['common_difference_max'],
    )
    number_of_terms = random.randint(
        RANDOM_RANGE['number_of_terms_min'],
        RANDOM_RANGE['number_of_terms_max'],
    )
    progression = [initial_term]
    for element in range(1, number_of_terms):
        progression.append(progression[element - 1] + common_difference)
    return progression


def stringify_progression(hidden_element, progression):
    """
    Get arithmetic progression as a list of str with an element to be guessed.

    Parameters:
        hidden_element: index of an element to be guessed;
        progression: arithmetic progression.

    Returns:
        progression as a list of strings with an element to be guessed.
    """
    string_progression = [str(element) for element in progression]
    string_progression[hidden_element] = '..'
    return ' '.join(string_progression)


def get_question_and_answer():
    """Evaluate the Q&A for the Guess-the-Progression-Element game.

    Returns:
        the game question and the correct answer.
    """
    progression = create_arithmetic_progression()
    hidden_element = random.choice(range(len(progression)))
    question = stringify_progression(hidden_element, progression)
    correct_answer = str(progression[hidden_element])
    return question, correct_answer
