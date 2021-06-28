from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


# -------- /start --------
def register_cmd_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, CommandStart())


async def cmd_start(message: types.Message):
    await message.reply("Hello!")


# -------- Command not found! --------
def register_cmd_not_found(dp: Dispatcher):
    dp.register_message_handler(cmd_not_found)


async def cmd_not_found(message: types.Message):
    await message.reply("Такой команды не существует\n"
                        "Список всех команд: /help")


handlers = [
    register_cmd_start,
    register_cmd_not_found
]
