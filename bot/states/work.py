from aiogram.dispatcher.filters.state import StatesGroup, State


class Parse_Name(StatesGroup):

    Name = State()


class Parse_Channel(StatesGroup):

    Channel = State()
