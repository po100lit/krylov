from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
import logging
from database import sqlite_db

logging.basicConfig(filename='krylov_bot.log', encoding='utf-8', level=logging.INFO, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Krylov is LOVE!', reply_markup=kb_client)
        await message.delete()
    except Exception as _ex:
        logging.warning(_ex)
        await message.reply('В этой группе работает бот, на некоторые сообщение он отвечает только в личку.\n'
                            'Ему запрещено первым начинать беседу - проявите инициативу =)\n'
                            'Начните диалог первым: https://t.me/krylov_ukg_bot\n'
                            'Бот обещал не СПАМить')


# @dp.message_handler(commands=['worktime'])
async def usual_open(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт: с 12:00 до 24:00, Пт-Сб: с 12:00 до 02:00')


# @dp.message_handler(commands=['address'])
async def location(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Крылова, д. 45')


@dp.message_handler(commands=['menu'])
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(usual_open, commands=['worktime'])
    dp.register_message_handler(location, commands=['address'])
    dp.register_message_handler(menu_command, commands=['menu'])
