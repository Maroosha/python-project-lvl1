"""Play an even-odd game with a user.

Continue untill there are 3 correct answers in a row.

"""

import random

import prompt


def oe_func(min_val, max_val):
    """Even-odd game. Play until 3 correct answers in a row.

    Parameters:
        min_val: min value in range of random int selection.
        max_val: max value in range of random int selection.

    Returns:
        congrats to the user :3

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
            if corr == 'yes':
                print("'no' is a wrong answer ;(. Correct answer was 'yes'.")
            if corr == 'no':
                print("'yes' is a wrong answer ;(. Correct answer was 'no'.")
            return "Let's try again, {0}!".format(name)
    return print('Congratulations, {0}!'.format(name))
