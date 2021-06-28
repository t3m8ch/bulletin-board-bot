from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from bulletin_board_bot.models import Ad

from bulletin_board_bot.dependencies import DIContainer

from bulletin_board_bot.keyboards import ad_browser_keyboard, ad_browser_cd


def register_cmd_browse_ads(dp: Dispatcher):
    dp.register_message_handler(cmd_browse_ads, Command("browseAds"))


async def cmd_browse_ads(message: types.Message, container: DIContainer):
    user_id = message.from_user.id
    ad_service = container.ad_service.get_service(user_id, True)

    text = get_message_text(await ad_service.next_ad())
    await message.answer(text, reply_markup=ad_browser_keyboard())


def register_cq_next_ad_handler(dp: Dispatcher):
    dp.register_callback_query_handler(cq_next_ad_handler,
                                       ad_browser_cd.filter(action="next"))


async def cq_next_ad_handler(call: types.CallbackQuery,
                             callback_data: dict,
                             container: DIContainer):
    user_id = call.from_user.id
    ad_service = container.ad_service.get_service(user_id)

    text = get_message_text(await ad_service.next_ad())
    await call.message.edit_text(text, reply_markup=ad_browser_keyboard())
    await call.answer()


def register_cq_back_ad_handler(dp: Dispatcher):
    dp.register_callback_query_handler(cq_back_ad_handler,
                                       ad_browser_cd.filter(action="back"))


async def cq_back_ad_handler(call: types.CallbackQuery,
                             callback_data: dict,
                             container: DIContainer):
    user_id = call.from_user.id
    ad_service = container.ad_service.get_service(user_id)

    text = get_message_text(await ad_service.back_ad())
    await call.message.edit_text(text, reply_markup=ad_browser_keyboard())
    await call.answer()


def get_message_text(ad: Ad):
    text = f"{ad.text}\n\n<b>Дата добавления: " \
           f"{ad.creation_date.strftime('%d.%m.%y %H:%M:%S')}</b>"
    return text


handlers = [
    register_cmd_browse_ads,
    register_cq_next_ad_handler,
    register_cq_back_ad_handler,
]
