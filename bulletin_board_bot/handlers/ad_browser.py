from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from bulletin_board_bot.services.ad_service import FakeAdService

from bulletin_board_bot.keyboards import ad_browser_keyboard, ad_browser_cd

ads = [
    "Ad1",
    "Ad2",
    "Ad3",
    "Ad4"
]


def get_handlers(user_data: dict):
    def register_cmd_browse_ads(dp: Dispatcher):
        dp.register_message_handler(cmd_browse_ads, Command("browseAds"))

    async def cmd_browse_ads(message: types.Message):
        user_id = message.from_user.id
        user_data[user_id] = {
            "ad_service": FakeAdService()
        }

        await message.answer(
            (await user_data[user_id]["ad_service"].next_ad()).text,
            reply_markup=ad_browser_keyboard()
        )

    def register_cq_next_ad_handler(dp: Dispatcher):
        dp.register_callback_query_handler(cq_next_ad_handler,
                                           ad_browser_cd.filter(action="next"))

    async def cq_next_ad_handler(call: types.CallbackQuery, callback_data: dict):
        user_id = call.from_user.id
        ad_service = user_data[user_id]["ad_service"]
        await call.message.edit_text(
            (await ad_service.next_ad()).text,
            reply_markup=ad_browser_keyboard()
        )
        await call.answer()

    def register_cq_back_ad_handler(dp: Dispatcher):
        dp.register_callback_query_handler(cq_back_ad_handler,
                                           ad_browser_cd.filter(action="back"))

    async def cq_back_ad_handler(call: types.CallbackQuery, callback_data: dict):
        user_id = call.from_user.id
        ad_service = user_data[user_id]["ad_service"]
        await call.message.edit_text(
            (await ad_service.back_ad()).text,
            reply_markup=ad_browser_keyboard()
        )
        await call.answer()

    return [
        register_cmd_browse_ads,
        register_cq_next_ad_handler,
        register_cq_back_ad_handler,
    ]
