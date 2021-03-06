"""Game engine and supporting functions."""

# !/usr/bin/env python3

import prompt

ROUNDS = 3


def run_engine(get_question_and_answer, game_rule):
    """Brain Games engine. Play untill 3 correct answers or 1 faillure.

    Parameters:
        get_question_and_answer: game question and correct answer;
        game_rule: game rule.

    Returns:
        nothing.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_rule)
    for _ in range(ROUNDS):
        question, correct_answer = get_question_and_answer()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                '"{0}" is wrong answer ;( '
                'Correct answer was "{1}".'.format(answer, correct_answer),
            )
            print("Let's try again, {0}!".format(name))
            return
    print('Congratulations, {0}!'.format(name))
