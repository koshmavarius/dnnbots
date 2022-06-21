import telebot
from telebot import types


next = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
nextbtn = types.KeyboardButton('🔥Продолжить')
next.add(nextbtn)

regphone = types.ReplyKeyboardMarkup(resize_keyboard=True)
regphonebtn = types.KeyboardButton('Зарегестрироваться',request_contact= True)
regphone.add(regphonebtn)

regloc = types.ReplyKeyboardMarkup(resize_keyboard=True)
reglocbtn = types.KeyboardButton('Зарегестрироваться',request_location= True)
regloc.add(reglocbtn)