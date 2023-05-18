from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging
from stopwords import stop_words
import string

logging.basicConfig(filename='krylov_bot.log', encoding='utf-8', level=logging.INFO, filemode='a',
                    format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
bot = Bot(token='6022406658:AAFRPGZGietE7xnd_X_tOYfnLw3gVNIPjIU')
dp = Dispatcher(bot)

logging.info('Bot is running...')


async def on_startup(_):
    print('Bot online!')


# Client
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Krylov is LOVE!')
        await message.delete()
    except Exception as _ex:
        logging.warning(_ex)
        await message.reply('В этой группе работает бот, на некоторые сообщение он отвечает только в личку.\n'
                            'Ему запрещено первым начинать беседу - проявите инициативу =)\n'
                            'Начните диалог первым: https://t.me/krylov_ukg_bot\n'
                            'Бот обещал не СПАМить')


@dp.message_handler(commands=['worktime'])
async def usual_open(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Вс-Чт: с 12:00 до 24:00, Пт-Сб: с 12:00 до 02:00') @ dp.message_handler(
        commands=['Режим работы'])


@dp.message_handler(commands=['address'])
async def location(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Крылова, д. 45')


# Admin

# Common

@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}.intersection(
            stop_words()) != set():
        await bot.send_message(message.from_user.id, 'Мат shall not pass\nОбратись к админу, если я не прав')
        await message.reply('Удалил сообщение, с подозрением на содержание мата')
        await message.delete()
    # if message.text == 'Hi':
    #     await message.answer('И сам не хворай!')  # отвечаем в чате тем же сообщением
    # await message.reply(message.text)  # отвечаем в чате тем же сообщением с цитированием
    # await bot.send_message(message.from_user.id, message.text)  # отвечаем в личку


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
logging.info('Bot stopped...')


def main():
    pass


if __name__ == '__main__':
    main()
