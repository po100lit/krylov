from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN_KR'))
dp = Dispatcher(bot)
