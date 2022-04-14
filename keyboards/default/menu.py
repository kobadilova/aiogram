from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Комедия"),
        ],
        [
            KeyboardButton(text="Мелодрама"),
            KeyboardButton(text="Фантастика")
        ],
    ],
    resize_keyboard=True
)