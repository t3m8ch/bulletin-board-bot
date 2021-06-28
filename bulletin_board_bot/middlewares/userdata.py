from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from bulletin_board_bot.user_data import UserDataStorage


class UserDataMiddleware(BaseMiddleware):
    def __init__(self, user_data_storage: UserDataStorage):
        super().__init__()
        self._user_data = user_data_storage

    async def on_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        data["user_data"] = self._user_data.for_user(user_id)

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        user_id = call.from_user.id
        data["user_data"] = self._user_data.for_user(user_id)
