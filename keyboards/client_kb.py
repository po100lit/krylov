from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/worktime')
b2 = KeyboardButton('/address')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('Отправить свой номер телефона',request_contact=True)
# b5 = KeyboardButton('Отправить своё местоположение', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# kb_client.add(b1).add(b2).add(b3)
# kb_client.add(b1).add(b2).insert(b3)
kb_client.row(b1, b2, b3)#.row(b4, b5)
