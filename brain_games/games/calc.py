"""Play Calculator game with a user."""

# !/usr/bin/env python3


import random

GAME_RULE = 'What is the result of the expression?'
MIN_VALUE, MAX_VALUE = 0, 101


def get_question_and_answer():
    """Evaluate Q&A for the Calculator game.

    Returns:
        the game question and the correct answer.
    """
    number1 = random.randint(MIN_VALUE, MAX_VALUE)
    number2 = random.randint(MIN_VALUE, MAX_VALUE)
    summ = '{0} + {1}'.format(number1, number2)
    difference = '{0} - {1}'.format(number1, number2)
    product = '{0} * {1}'.format(number1, number2)
    questions_to_answers = {
        summ: number1 + number2,
        difference: number1 - number2,
        product: number1 * number2,
    }
    question = random.choice(list(questions_to_answers.keys()))
    correct_answer = str(questions_to_answers[question])
    return question, correct_answer
