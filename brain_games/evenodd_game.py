"""Play an even-odd game with a user.

Continue untill there are 3 correct answers in a row or a single failure.

"""

import random

import prompt


def oe_func(min_val, max_val):
    """Even-odd game. Play until 3 correct answers in a row or 1 failure.

    Parameters:
        min_val: min value in range of random int selection.
        max_val: max value in range of random int selection.

    Returns:
        congrats :3 or condolences :(

    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        num = random.randint(min_val, max_val)
        if num % 2 == 0:
            corr = 'yes'
        else:
            corr = 'no'
        print('Question: {0}'.format(num))
        answer = prompt.string('Your answer: ')
        if answer == corr:
            print('Correct!')
            count += 1
        else:
            print(
                '"{0}" is a wrong answer ;( '
                'The correct answer is "{1}".'.format(answer, corr))
            return "Let's try again, {0}!".format(name)
    return print('Congratulations, {0}!'.format(name))
