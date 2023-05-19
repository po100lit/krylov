from aiogram.utils import executor
from create_bot import dp
import logging
from handlers import client, admin, other

logging.basicConfig(filename='krylov_bot.log', encoding='utf-8', level=logging.INFO, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Bot is running...')


async def on_startup(_):
    print('Bot online!')


client.register_handlers_client(dp)
# client.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

logging.info('Bot stopped...')

if __name__ == '__main__':
    pass
