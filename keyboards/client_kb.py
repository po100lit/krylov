from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/worktime')
b2 = KeyboardButton('/address')
b3 = KeyboardButton('/Menu')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2).add(b3)
