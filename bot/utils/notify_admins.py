import logging

from data.config import ADMIN_ID

from aiogram import Dispatcher



async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN_ID, "<a><pre>The bot has started!</pre></a>", parse_mode = 'HTML')

    except Exception as err:
        logging.exception(err)
