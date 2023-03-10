from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

new_student = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đ Registratsiadan o'tish"),
            KeyboardButton(text="đ Kurslar haqida")
        ],
        [
            KeyboardButton(text="âšī¸ O'quv markazi haqida")
        ]
    ],
    resize_keyboard=True
)

subjects = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đĸ Matematika"),
            KeyboardButton(text="đ Ingliz tili"),
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
