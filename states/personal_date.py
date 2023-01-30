from aiogram.dispatcher.filters.state import State, StatesGroup


class PersonalData(StatesGroup):
    full_name = State()
    phone_number = State()
    subject = State()
    responce = State()
