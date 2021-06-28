from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


ad_browser_cd = CallbackData("ad_browser", "action")


def ad_browser_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🠔 Предыдущее",
                callback_data=ad_browser_cd.new(action="back")
            ),
            InlineKeyboardButton(
                text="В избранное",
                callback_data=ad_browser_cd.new(action="favorites")
            ),
            InlineKeyboardButton(
                text="Следующее 🠖",
                callback_data=ad_browser_cd.new(action="next")
            ),
        ],
    ])
