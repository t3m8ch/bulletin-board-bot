from aiogram import Dispatcher

from bulletin_board_bot.handlers import common, ad_browser


def register_handlers(dp: Dispatcher, user_data: dict):
    """A function that registers all handlers
    Example of registration of several handlers:
    .. code-block:: python

       handlers =
           module1.handlers + \
           module2.handlers + \
           module3.handlers

    Each handler module must contain a list of 'handlers',
    which stores the functions that register the handler.

    Remember that the order of handlers is important!
    """
    handlers = \
        ad_browser.get_handlers(user_data) + \
        common.handlers

    for handler in handlers:
        handler(dp)
