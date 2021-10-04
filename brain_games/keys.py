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
    return message, func
