# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


start_work = InlineKeyboardMarkup(row_width=2)
but_1 = InlineKeyboardButton(text='📕 Search by name', callback_data='📕 Search by name')
but_2 = InlineKeyboardButton(text='📗 Channel search', callback_data='📗 Channel search')
but_3 = InlineKeyboardButton(text='📘 Search by trends', callback_data='📘 Search by trends')
start_work.add(but_1)
start_work.add(but_2)
start_work.add(but_3)
