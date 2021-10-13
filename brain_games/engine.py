"""Game engine and supporting functions."""

# !/usr/bin/env python3

import prompt

ATTEMPT_NO = 3


def run_engine(game_function, game_rule, attempts=ATTEMPT_NO):
    """Brain Games engine. Play untill 3 correct answers or 1 faillure.

    Parameters:
        game_function: game function;
        game_rule: game rule;
        attempts: max number of attempts (constant).

    Returns:
        nothing.

    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_rule)
    for _ in range(attempts):
        question, corr = game_function()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == corr:
            print('Correct!')
        else:
            print(
                '"{0}" is wrong answer ;( '
                'Correct answer was "{1}".'.format(answer, corr),
            )
            print("Let's try again, {0}!".format(name))
            return
    print('Congratulations, {0}!'.format(name))
    return
