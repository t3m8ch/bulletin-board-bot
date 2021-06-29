from aiogram import Dispatcher

from bulletin_board_bot.handlers import common, ad_browser


def register_handlers(dp: Dispatcher):
    r"""A function that registers all handlers
    Example of registration of several handlers:
    .. code-block:: python

       router = [
            module1.router,
            module2.router,
       ]

    Each handler module must contain a Router object,
    which stores the functions that register the handler.

    Remember that the order of routers is important!
    """
    routers = [
        ad_browser.router,
        common.router,
    ]

    for router in routers:
        router.register_handlers(dp)
