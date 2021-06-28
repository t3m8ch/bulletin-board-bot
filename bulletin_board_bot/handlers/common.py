from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


# -------- /start --------
def register_cmd_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, CommandStart())


async def cmd_start(message: types.Message):
    text = "Привет! Это доска объявлений. Здесь ты сможешь опубликовать своё объявление, " \
           "которое увидят сотни пользователей.\n\n" \
           "Используй команду /newAd. Если ты хочешь посмотреть чужие объявления, выполни /browseAds.\n\n" \
           "Чтобы посмотреть все команды, пиши /help."
    await message.reply(text)


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
