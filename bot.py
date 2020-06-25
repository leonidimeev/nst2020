# !/usr/bin/env python3
#
# NST2020 bot 
# 
#
#

import config
import telebot
from time import sleep
from parser import *
#from telebot import types
import threading

# buttons of groups
# markup = types.ReplyKeyboardMarkup()

bot = telebot.TeleBot(config.token)	


# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, '''
Это бот - парсер учебного расписания для студентов СВФУ
Введите название группы в формате (пример): ИМИ-БА-ПМИ-17 ,
заполненное расписание сейчас есть у группы ИФ-БА-ПОИ-19''')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
	print(type(message.text))
	timetable = get_timetable(message.text)
	bot.send_message(message.chat.id, timetable)

# def get_groups_every_1hour():

# 	markup.row('a', 'v')
# 	markup.row('c', 'd', 'e')

if __name__ == '__main__':
	# timer = threading.Timer(1440.0, get_groups_every_1hour) 
	# timer.start()

	while True:
		try:
			bot.polling(none_stop=True)
		except Exception as e:
			sleep(15)




