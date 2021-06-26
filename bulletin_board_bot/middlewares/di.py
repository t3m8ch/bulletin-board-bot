from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from bulletin_board_bot.dependencies import DIContainer


class DIContainerMiddleware(BaseMiddleware):
    def __init__(self, container: DIContainer):
        super().__init__()
        self._container = container

    async def on_process_message(self, message: types.Message, data: dict):
        data["container"] = self._container

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        data["container"] = self._container
