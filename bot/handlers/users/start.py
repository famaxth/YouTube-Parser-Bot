from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data.config import ADMIN_ID
from keyboards.keyboards import start_work


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await dp.bot.send_message(message.chat.id, "Hello!\n\nI will help you find the right videos on the Youtube platform. To get started, select the necessary action:", reply_markup=start_work)
