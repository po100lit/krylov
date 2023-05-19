from aiogram import types, Dispatcher
from create_bot import dp, bot
from stopwords import stop_words

# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', '!"#$%&()*+,-.:;<=>?@[\]^_`{|}~'))
            for i in message.text.split()}.intersection(stop_words()) != set():
        await bot.send_message(message.from_user.id, 'Мат shall not pass\nОбратись к админу, если я не прав')
        await message.reply('Удалил сообщение, с подозрением на содержание мата')
        await message.delete()
    else:
        await message.reply('Извините, я не знаю эту команду\nВоспользуйтесь меню')
    # if message.text == 'Hi':
    #     await message.answer('И сам не хворай!')  # отвечаем в чате тем же сообщением
    # await message.reply(message.text)  # отвечаем в чате тем же сообщением с цитированием
    # await bot.send_message(message.from_user.id, message.text)  # отвечаем в личку


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
