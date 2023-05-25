import sqlite3 as sq
import logging
from create_bot import bot, dp

logging.basicConfig(filename='krylov_bot.log', encoding='utf-8', level=logging.INFO, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def sql_start():
    global base, cur
    base = sq.connect('krylov.db')
    cur = base.cursor()
    if base:
        logging.info('Database connected')
        print('Database connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * from menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f"{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}")