from aiogram import Dispatcher

from bulletin_board_bot.dependencies import DIContainer
from bulletin_board_bot.middlewares.di import DIContainerMiddleware
from bulletin_board_bot.middlewares.userdata import UserDataMiddleware


def setup_middlewares(dp: Dispatcher,
                      user_data: dict,
                      container: DIContainer):
    dp.setup_middleware(UserDataMiddleware(user_data))
    dp.setup_middleware(DIContainerMiddleware(container))
