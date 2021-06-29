from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


ad_browser_cd = CallbackData("ad_browser", "action")


def ad_browser_keyboard(ad_in_favorites: bool = False) -> InlineKeyboardMarkup:
    favorites_btn_text = "Удалить из избранного ❌" if ad_in_favorites else "В избранное ★"
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=favorites_btn_text,
                callback_data=ad_browser_cd.new(action="favorites")
            ),
        ],
        [
            InlineKeyboardButton(
                text="← Предыдущее",
                callback_data=ad_browser_cd.new(action="back")
            ),
            InlineKeyboardButton(
                text="Следующее →",
                callback_data=ad_browser_cd.new(action="next")
            ),
        ]
    ])
