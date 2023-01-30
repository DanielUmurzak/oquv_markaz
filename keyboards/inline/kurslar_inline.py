from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kurlar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔢 Matematika", callback_data="matematika_button"),
        ],
        [
            InlineKeyboardButton(text="📙 Ingliz tili", callback_data="english_button"),
        ],
        [
            InlineKeyboardButton(text="Va boshqa kurslar", callback_data="va_boshqalar"),

        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="ortga_button"),

        ]
    ]
)
ortga_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="from_subject_tosubjects")
        ]
    ]
)
info_ortga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="from_oquv_markaz_info_to_yangi")
        ]
    ]
)
