from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oquv markazi o'quvchisi🎓")
        ],
        [
            KeyboardButton(text="Yangi o'quvchi 📚")
        ]
    ],
    resize_keyboard=True
)

Start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 IELTS"),
            KeyboardButton(text="💻 Programming"),
        ],
        [
            KeyboardButton(text="📚 Eng kop soraladigan asarlar"),

        ]
    ],
    resize_keyboard=True
)
