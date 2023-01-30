from aiogram import types
from aiogram.types import Message, CallbackQuery

from keyboards.default.kirish_button import start_button
from keyboards.default.yangi_oquvchi_button import new_student
from keyboards.inline.kurslar_inline import info_ortga
from loader import dp


@dp.message_handler(text="Yangi o'quvchi 📚")
async def yangi_oquvchi_func(msg: Message):
    pic = open("D:/programming/Telegram_bots/aiogram-atates-oquv_markazi/photos/hush.jpg", "rb")
    text = "Xush kelibsiz"
    await msg.answer_photo(pic, text, reply_markup=new_student)


@dp.message_handler(text="ℹ️ O'quv markazi haqida")
async def oquv_markazi_info_function(msg: Message):
    text = "O'quv markazi to'grisida informatsia: "
    pic = open("D:/programming/Telegram_bots/aiogram-atates-oquv_markazi/photos/study_center.png", "rb")
    await msg.answer_photo(pic, text, reply_markup=info_ortga)


@dp.callback_query_handler(text="from_oquv_markaz_info_to_yangi")
async def info_delet(call: CallbackQuery):
    text = "Xush kelibsiz"
    await call.message.answer(text)
    await call.message.delete()


@dp.message_handler(text="↩️ Ortga")
async def ortga_func(msg: Message):
    await msg.answer(f"Salom, {msg.from_user.full_name}!", reply_markup=start_button)
