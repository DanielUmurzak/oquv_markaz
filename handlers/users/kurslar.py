from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from keyboards.default.yangi_oquvchi_button import new_student
from keyboards.inline.kurslar_inline import kurlar_button, ortga_button
from loader import dp


@dp.message_handler(text="📚 Kurslar haqida")
async def kurslar_func(msg: Message):
    await msg.answer("Bizning kurslar: ", reply_markup=kurlar_button)


@dp.callback_query_handler(text="matematika_button")
async def matem_func(call: CallbackQuery):
    text = "Matematika"
    pic = open("D:/programming/Telegram_bots/aiogram-atates-oquv_markazi/photos/eaa9a531c2ef7821076769cd8d093dd5.jpg",
               "rb")
    await call.message.answer_photo(pic, text, reply_markup=ortga_button)
    await call.message.delete()


@dp.callback_query_handler(text="english_button")
async def english_button_func(call: CallbackQuery):
    text = "English"
    pic = open("D:/programming/Telegram_bots/aiogram-atates-oquv_markazi/photos/english.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=ortga_button)
    await call.message.delete()


@dp.callback_query_handler(text="from_subject_tosubjects")
async def from_subject_tosubjects_func(call: CallbackQuery):
    await call.message.answer("Bizning kurslar:", reply_markup=kurlar_button)
    await call.message.delete()


@dp.callback_query_handler(text="ortga_button")
async def yangi_oquvchiga_func(call: CallbackQuery):
    text = "👇 Quyidagilardan birini tanlang 👇"
    await call.message.answer(text, reply_markup=new_student)
    await call.message.delete()
