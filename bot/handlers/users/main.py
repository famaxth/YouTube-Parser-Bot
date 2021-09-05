# -*- coding: utf-8 -*-

from time import sleep

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp
from youtube import YouTube
from states.work import Parse_Name, Parse_Channel


@dp.callback_query_handler(lambda c: c.data == '📕 Search by name', state=None)
async def by_name(call: types.CallbackQuery, state: FSMContext):
    await dp.bot.send_message(call.message.chat.id, "✏️ Enter the text:")
    await Parse_Name.Name.set()


@dp.message_handler(state=Parse_Name.Name)
async def search_by_name(message: types.Message, state: FSMContext):
    try:
        start = YouTube()
        await dp.bot.send_message(message.chat.id, "Starting the search...")
        result = start.search_videos(user_text=message.text)
        await dp.bot.send_message(message.chat.id, "✅ Information received:\n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]), disable_web_page_preview=True)
        await state.finish()
    except:
        await dp.bot.send_message(message.chat.id, "❌ Error! Nothing was found.")
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == '📗 Channel search', state=None)
async def by_channel(call: types.CallbackQuery, state: FSMContext):
    await dp.bot.send_message(call.message.chat.id, "✏️ Enter the link to the channel:")
    await Parse_Channel.Channel.set()


@dp.message_handler(state=Parse_Channel.Channel)
async def search_by_channel(message: types.Message, state: FSMContext):
    try:
        start = YouTube()
        await dp.bot.send_message(message.chat.id, "Starting the search...")
        result = start.search_videos_from_channel(user_url=message.text)
        await dp.bot.send_message(message.chat.id, "✅ Information received:\n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]), disable_web_page_preview=True)
        await state.finish()
    except:
        await dp.bot.send_message(message.chat.id, "❌ Error! Nothing was found.")
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == '📘 Search by trends', state=None)
async def by_trends(call: types.CallbackQuery, state: FSMContext):
    try:
        start = YouTube()
        await dp.bot.send_message(call.message.chat.id, "Starting the search...")
        result = start.search_youtube_trends()
        await dp.bot.send_message(call.message.chat.id, "✅ Information received:\n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]), disable_web_page_preview=True)
        await state.finish()
    except:
        await dp.bot.send_message(call.message.chat.id, "❌ Error! Nothing was found.")
        await state.finish()
