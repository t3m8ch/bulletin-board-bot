from aiogram import types
from aiogram.dispatcher.filters import Command
from bulletin_board_bot.misc.router import Router

from bulletin_board_bot.models import AdModel

from bulletin_board_bot.dependencies import DIContainer

from bulletin_board_bot.keyboards import ad_browser_keyboard, ad_browser_cd

router = Router()


# -------- /browseAds --------
@router.message(Command("browseAds"))
async def cmd_browse_ads(message: types.Message,
                         user_data: dict,
                         container: DIContainer):
    user_id = message.from_user.id
    ad_service = container.ad_service.get_service(user_id, True)
    
    ad = await ad_service.next_ad()
    user_data["current_ad"] = ad
    
    text = get_message_text(ad)
    await message.answer(text, reply_markup=ad_browser_keyboard(ad.in_favorites))


# -------- Next ad callback query --------
@router.callback_query(ad_browser_cd.filter(action="next"))
async def cq_next_ad_handler(call: types.CallbackQuery,
                             callback_data: dict,
                             user_data: dict,
                             container: DIContainer):
    user_id = call.from_user.id
    ad_service = container.ad_service.get_service(user_id)

    ad = await ad_service.next_ad()
    user_data["current_ad"] = ad

    text = get_message_text(ad)
    await call.message.edit_text(text, reply_markup=ad_browser_keyboard(ad.in_favorites))
    await call.answer()


# -------- Back ad callback query --------
@router.callback_query(ad_browser_cd.filter(action="back"))
async def cq_back_ad_handler(call: types.CallbackQuery,
                             callback_data: dict,
                             user_data: dict,
                             container: DIContainer):
    user_id = call.from_user.id
    ad_service = container.ad_service.get_service(user_id)

    ad = await ad_service.back_ad()
    user_data["current_ad"] = ad

    text = get_message_text(ad)
    await call.message.edit_text(text, reply_markup=ad_browser_keyboard(ad.in_favorites))
    await call.answer()


# -------- Add or remove ad in favorites callback query --------
@router.callback_query(ad_browser_cd.filter(action="favorites"))
async def cq_toggle_favorite(call: types.CallbackQuery,
                             callback_data: dict,
                             user_data: dict,
                             container: DIContainer):
    user_id = call.from_user.id
    user_service = container.user_service.get_service()

    ad = user_data["current_ad"]
    if ad.in_favorites:
        await user_service.remove_ad_from_favorites(ad, user_id)
        await call.answer(
            text="Объявление успешно удалено из избранных!",
            show_alert=True
        )
    else:
        await user_service.add_ad_to_favorites(ad, user_id)
        await call.answer(
            text="Объявление успешно добавлено в избранное!",
            show_alert=True
        )

    text = call.message.text
    await call.message.edit_text(text, reply_markup=ad_browser_keyboard(ad.in_favorites))


# -------- Common --------
def get_message_text(ad: AdModel):
    text = f"{ad.text}\n\n<b>Дата добавления: " \
           f"{ad.creation_date.strftime('%d.%m.%y %H:%M:%S')}</b>"
    return text
