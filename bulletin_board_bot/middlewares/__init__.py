from aiogram import Dispatcher
from bulletin_board_bot.user_data import UserDataStorage

from bulletin_board_bot.dependencies import DIContainer
from bulletin_board_bot.middlewares.di import DIContainerMiddleware
from bulletin_board_bot.middlewares.userdata import UserDataMiddleware


def setup_middlewares(dp: Dispatcher,
                      user_data_storage: UserDataStorage,
                      container: DIContainer):
    dp.setup_middleware(UserDataMiddleware(user_data_storage))
    dp.setup_middleware(DIContainerMiddleware(container))
