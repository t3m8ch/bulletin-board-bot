from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class UserDataMiddleware(BaseMiddleware):
    def __init__(self, user_data: dict):
        super().__init__()
        self._user_data = user_data

    async def on_process_message(self, message: types.Message, data: dict):
        data["user_data"] = self._user_data

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        data["user_data"] = self._user_data
