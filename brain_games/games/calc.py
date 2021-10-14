"""Play Calculator game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'What is the result of the expression?'
MIN_VALUE, MAX_VALUE = 0, 101


def calc_evaluate_qa(min_value=MIN_VALUE, max_value=MAX_VALUE):
    """Evaluate Q&A for the Calculator game.

    Parameters:
        min_value: minimum in the range of random values;
        max_value: maximum in the range of random values.

    Returns:
        the game question and the correct answer.

    """
    number1 = random.randint(min_value, max_value)
    number2 = random.randint(min_value, max_value)
    summ = '{0} + {1}'.format(number1, number2)
    remainder = '{0} - {1}'.format(number1, number2)
    product = '{0} * {1}'.format(number1, number2)
    operations = {
        summ: number1 + number2,
        remainder: number1 - number2,
        product: number1 * number2,
    }
    question = random.choice(list(operations.keys()))
    correct_answer = str(operations[question])
    return question, correct_answer
