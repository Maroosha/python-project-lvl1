"""Game engine and supporting functions."""

# !/usr/bin/env python3

import prompt


def welcome_user():
    """Welcome the user.

    Returns:
        welcome message.

    """
    return 'Welcome to the Brain Games!'


def run_engine(func, message):
    """Brain Games engine. Play untill 3 correct answers or 1 faillure.

    Parameters:
        func: game function;
        message: game message..

    Returns:
        nothing.

    """
    print(welcome_user())
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(message)
    count = 0
    while count < 3:
        question, corr = func()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == corr:
            print('Correct!')
            count += 1
        else:
            print(
                '"{0}" is wrong answer ;( '
                'Correct answer was "{1}".'.format(answer, corr),
            )
            print("Let's try again, {0}!".format(name))
            break
    if count == 3:
        print('Congratulations, {0}!'.format(name))
    return
