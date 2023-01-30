from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

new_student = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Registratsiadan o'tish"),
            KeyboardButton(text="📚 Kurslar haqida")
        ],
        [
            KeyboardButton(text="ℹ️ O'quv markazi haqida")
        ]
    ],
    resize_keyboard=True
)

subjects = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔢 Matematika"),
            KeyboardButton(text="📙 Ingliz tili"),
        ],
        [
            KeyboardButton(text="Va boshqalar")
        ]
    ],
    resize_keyboard=True
)

res_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ]
    ],
    resize_keyboard=True
)
