# !/usr/bin/env python3
#
# NST2020 bot 
# 
#
#

import config
import telebot
from time import sleep
import parser
# from telebot import types
import threading
# подключение dialogflow ai
import dialogflow_ai

# buttons of groups
# markup = types.ReplyKeyboardMarkup()

bot = telebot.TeleBot(config.token)	
bot.remove_webhook() # отключает вебхук

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, '''
Это бот - парсер учебного расписания для студентов СВФУ
Введите название группы в формате (пример): ИМИ-БА-ПМИ-17 ,
заполненное расписание сейчас есть у группы ИФ-БА-ПОИ-19''')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def what_message(message):
	print('кто то написал ' + message.text)
	A = dialogflow_ai.send_to_dialogflow(message.text)
	if (A[1] == 'Get_timetable'):
		get_(message)
	else:
		bot.send_message(message.chat.id, A[3])


def get_(message):
	timetable = parser.get_timetable(message.text)
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




