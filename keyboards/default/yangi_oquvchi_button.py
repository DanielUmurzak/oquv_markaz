from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

new_student = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Registratsiadan o'tish"),
            KeyboardButton(text="📚 Kurslar haqida")
        ],
        [
            KeyboardButton(text="ℹ️ O'quv markazi haqida"),
            KeyboardButton(text="↩️ Ortga")
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
