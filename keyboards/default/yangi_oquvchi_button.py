from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

new_student = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đ Registratsiadan o'tish"),
            KeyboardButton(text="đ Kurslar haqida")
        ],
        [
            KeyboardButton(text="âšī¸ O'quv markazi haqida"),
            KeyboardButton(text="âŠī¸ Ortga")
        ]
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True)
        ]
    ],
    resize_keyboard=True
)
