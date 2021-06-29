from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from bulletin_board_bot.router import Router

router = Router()


# -------- /start --------
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    text = "Привет! Это доска объявлений. Здесь ты сможешь опубликовать своё объявление, " \
           "которое увидят сотни пользователей.\n\n" \
           "Используй команду /newAd. Если ты хочешь посмотреть чужие объявления, выполни /browseAds.\n\n" \
           "Чтобы посмотреть все команды, пиши /help."
    await message.reply(text)


# -------- Command not found! --------
@router.message()
async def cmd_not_found(message: types.Message):
    await message.reply("Такой команды не существует\n"
                        "Список всех команд: /help")


handlers = [
    router.register_handlers
]
