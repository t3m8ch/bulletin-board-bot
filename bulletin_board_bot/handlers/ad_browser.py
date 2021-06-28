from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from bulletin_board_bot.models import Ad

from bulletin_board_bot.dependencies import DIContainer

from bulletin_board_bot.keyboards import ad_browser_keyboard, ad_browser_cd


# -------- /browseAds --------
def register_cmd_browse_ads(dp: Dispatcher):
    dp.register_message_handler(cmd_browse_ads, Command("browseAds"))


async def cmd_browse_ads(message: types.Message, 
                         user_data: dict,
                         container: DIContainer):
    user_id = message.from_user.id
    ad_service = container.ad_service.get_service(user_id, True)
    
    ad = await ad_service.next_ad()
    user_data["current_ad"] = ad
    
    text = get_message_text(ad)
    await message.answer(text, reply_markup=ad_browser_keyboard())


# -------- Next ad callback query --------
def register_cq_next_ad_handler(dp: Dispatcher):
    dp.register_callback_query_handler(cq_next_ad_handler,
                                       ad_browser_cd.filter(action="next"))


async def cq_next_ad_handler(call: types.CallbackQuery,
                             callback_data: dict,
                             user_data: dict,
                             container: DIContainer):
    user_id = call.from_user.id
    ad_service = container.ad_service.get_service(user_id)

    ad = await ad_service.next_ad()
    user_data["current_ad"] = ad

    text = get_message_text(ad)
    await call.message.edit_text(text, reply_markup=ad_browser_keyboard())
    await call.answer()


# -------- Back ad callback query --------
def register_cq_back_ad_handler(dp: Dispatcher):
    dp.register_callback_query_handler(cq_back_ad_handler,
                                       ad_browser_cd.filter(action="back"))


async def cq_back_ad_handler(call: types.CallbackQuery,
                             callback_data: dict,
                             user_data: dict,
                             container: DIContainer):
    user_id = call.from_user.id
    ad_service = container.ad_service.get_service(user_id)

    ad = await ad_service.back_ad()
    user_data["current_ad"] = ad

    text = get_message_text(ad)
    await call.message.edit_text(text, reply_markup=ad_browser_keyboard())
    await call.answer()


# -------- Add ad to favourites callback query --------
def register_cq_add_ad_to_favorites(dp: Dispatcher):
    dp.register_callback_query_handler(cq_add_ad_to_favorites,
                                       ad_browser_cd.filter(action="favorites"))


async def cq_add_ad_to_favorites(call: types.CallbackQuery,
                                 callback_data: dict,
                                 user_data: dict,
                                 container: DIContainer):
    user_id = call.from_user.id
    user_service = container.user_service.get_service()

    ad_id = user_data["current_ad"].id
    await user_service.add_ad_to_favorites(ad_id, user_id)

    await call.answer(
        text="Объявление успешно добавлено в избранное!",
        show_alert=True
    )


# -------- Common --------
def get_message_text(ad: Ad):
    text = f"{ad.text}\n\n<b>Дата добавления: " \
           f"{ad.creation_date.strftime('%d.%m.%y %H:%M:%S')}</b>"
    return text


handlers = [
    register_cmd_browse_ads,
    register_cq_next_ad_handler,
    register_cq_back_ad_handler,
    register_cq_add_ad_to_favorites,
]
