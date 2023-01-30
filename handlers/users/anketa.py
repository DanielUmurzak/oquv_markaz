from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.kirish_button import start_button
from keyboards.default.registratsiya import subjects, res_button
from states.personal_date import PersonalData
from loader import dp


@dp.message_handler(text="📋 Registratsiadan o'tish")
async def registration_func(msg: Message):
    await msg.answer("To'liq ismingizni kiriting 👇", reply_markup=ReplyKeyboardRemove())
    await PersonalData.full_name.set()


@dp.message_handler(state=PersonalData.full_name)
async def answer_fullname(msg: Message, state: FSMContext):
    fullname = msg.text
    await state.update_data(
        {"name": fullname}
    )
    await msg.answer("Telefon raqamingizni kiriting: ", reply_markup=ReplyKeyboardRemove())
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phone_number)
async def phone_function(msg: Message, state: FSMContext):
    phone_number = msg.text
    await state.update_data(
        {"number": phone_number}
    )
    await msg.answer("Qaysi fandan o'quv kursiga yozilmoqchisiz ?", reply_markup=subjects)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.subject)
async def phone_function(msg: Message, state: FSMContext):
    subject = msg.text
    await state.update_data(
        {"subject": subject}
    )
    data = await state.get_data()
    name = data.get("name")
    phone_number = data.get("number")
    subject = data.get("subject")

    text = f"Quidagi ma'lumotlar qabul qilindi: \n" \
           f"\n" \
           f"Ismingiz: {name} \n" \
           f"\n" \
           f"Raqamingiz: {phone_number} \n" \
           f"\n" \
           f"Tanlagan faningiz: {subject} \n" \
           f"\n" \
           f"Agar berilgan malumotlar to'gri bo'lsa Ha ni, to'g'irlamoqchi bo'lsangiz Yo'q ni bosin"

    await msg.answer(text, reply_markup=res_button)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.responce)
async def phone_function(msg: Message, state: FSMContext):
    responce = msg.text
    if responce == "Ha":
        data = await state.get_data()
        name = data.get("name")
        phone_number = data.get("number")
        subject = data.get("subject")

        text = f"Ism: {name} \n" \
               f"\n" \
               f"Raqam: {phone_number} \n" \
               f"\n" \
               f"Tanlagan fan: {subject} \n" \
               f"\n"
        for admin in ADMINS:
            await dp.bot.send_message(admin, text)
        await msg.answer(f"Salom, {msg.from_user.full_name}!", reply_markup=start_button)
        await state.finish()

    elif responce == "Yo'q":
        await msg.answer("To'liq ismingizni kiriting 👇", reply_markup=ReplyKeyboardRemove())
        await PersonalData.full_name.set()
