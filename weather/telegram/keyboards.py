from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

MAIN_KBD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Узнать погоду",
                switch_inline_query_current_chat="",
            )
        ]
    ]
)
