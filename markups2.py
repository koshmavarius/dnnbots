import telebot
from telebot import types

next = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
nextbtn = types.KeyboardButton('🔞Продолжить')
next.add(nextbtn)

yesno = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
yes = types.KeyboardButton('Да')
no = types.KeyboardButton('Нет')
yesno.add(yes,no)


regphone = types.ReplyKeyboardMarkup(resize_keyboard=True)
regphonebtn = types.KeyboardButton('Зарегестрироваться',request_contact= True)
regphone.add(regphonebtn)

regloc = types.ReplyKeyboardMarkup(resize_keyboard=True)
reglocbtn = types.KeyboardButton('Зарегестрироваться',request_location= True)
regloc.add(reglocbtn)