from aiogram import Dispatcher
from bulletin_board_bot.middlewares.userdata import UserDataMiddleware


def setup_middlewares(dp: Dispatcher, user_data: dict):
    dp.setup_middleware(UserDataMiddleware(user_data))
