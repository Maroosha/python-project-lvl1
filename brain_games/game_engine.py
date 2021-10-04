"""Game engine and supporting functions."""

# !/usr/bin/env python3

import prompt

import brain_games.keys


def welcome_user():
    """Welcome the user.

    Returns:
        welcome message.

    """
    return 'Welcome to the Brain Games!'


def engine(keyword):
    """Brain Games engine. Play untill 3 correct answers or 1 faillure.

    Parameters:
        keyword: keyword of the game to be played.

    Returns:
        game output.

    """
    message, func = brain_games.keys.keyfunc(keyword)
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
                '"{0}" is a wrong answer ;( '
                'The correct answer is "{1}".'.format(answer, corr),
            )
            return "Let's try again, {0}!".format(name)
    return 'Congratulations, {0}!'.format(name)
