"""Game keywords."""

# !/usr/bin/env python3


def keyfunc(keyword):
    """Import a corresponing game module.

    Parameters:
        keyword: name of a game script.

    Returns:
        game message and game function.
    """
    if keyword == 'brain-even':
        from brain_games.games.evenodd_game import func, message
    elif keyword == 'brain-calc':
        from brain_games.games.calc_game import func, message
    elif keyword == 'brain-gcd':
        from brain_games.games.gcd_game import func, message
    elif keyword == 'brain-progression':
        from brain_games.games.progression_game import func, message
    else:   # elif keyword == 'brain-prime':
        from brain_games.games.prime_game import func, message
    return message, func
