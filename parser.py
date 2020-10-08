# !/usr/bin/env python3
#
# Timetable - parser script for NST2020
# 
# urok gita u ft 09.10.2020
#

import urllib.request
from bs4 import BeautifulSoup
import requests

# def get_html(url):
# 	response = urllib.request.urlopen(url)
# 	return response.read()

def beautiful_out(content):
	text = BeautifulSoup(content, features = "html.parser").text.replace('\t', '')
	while '\n\n' in text:
		text = text.replace('\n\n', '\n')
	text = text.split('\n')
	return(text)

def post_request_of_group(html,groupname):
	import datetime
	headers = {
		"User-Agent": "Chat-bot of students 0.1"
	}
	ttinfo = {
		"action": "showrasp",
	    "groupname": groupname,
	    "mydate": datetime.datetime.now().strftime("%d-%m-%Y")

	}
	r = requests.post(html,  headers=headers, data=ttinfo)
	return(r)

# Output - functions:
def out_week(content):
	wo_content = week_out_content(content)
	week = wo_content[0]
	weekdays = wo_content[1]
	OUT = ''
	for i in range(1,7):
		OUT += week[i]
		OUT += '\n'
		for lesson in weekdays[i]:
			OUT += lesson
			OUT += '\n'
		OUT += '\n'
	return(OUT)

def out_some_day(content, day):
	wo_content = week_out_content(content)
	week = wo_content[0]
	weekdays = wo_content[1]
	print(week[day])
	for lesson in weekdays[day]:
		print(lesson)

def out_some_day_some_lesson(content, day, lesson_number):
	wo_content = week_out_content(content)
	week = wo_content[0]
	weekdays = wo_content[1]
	times = wo_content[2]
	lesson = wo_content[3]
	print(week[day])
	
	print('----------------------')
	print(times)

def week_out_content(content):
	weekdays = []
	times = []
	lessons = []
	teachers = []
	classrooms = []
	for i in range(7):
		weekdays.append([])
		times.append([])
		lessons.append([])
		teachers.append([])
		classrooms.append([])
	week = { 1: 'ПОНЕДЕЛЬНИК', 2: 'ВТОРНИК', 3: 'СРЕДА', 4: 'ЧЕТВЕРГ', 5: 'ПЯТНИЦА', 6: 'СУББОТА' }
	lesson_time = { 1: '08:00-09:35', 2: '09:50-11:25', 3: '11:40-13:15', 4:'14:00-15:35', 5:'15:50-17:25', 6:'17:30-19:05' }
	
	wd = 0
	
	i = 7
	while True:
		try:
			for key in week:
				if week[key] in content[i - 1]:
					wd = key
			# times[wd].append(lesson_time[content[i]])
			times[wd].append(content[i])
			lessons[wd].append(content[i+1])
			teachers[wd].append(content[i+2])
			classrooms[wd].append(content[i+3])

			weekdays[wd].append(content[i])
			weekdays[wd].append(content[i+1])
			weekdays[wd].append(content[i+2])
			weekdays[wd].append(content[i+3])
		except:
			break
		i += 5
	return(week,weekdays,times,lessons,teachers,classrooms)

def get_timetable(groupname):
	html = "https://s-vfu.ru/raspisanie/ajax.php"
	# groupname = "ИФ-БА-ПОИ-19"
	content = post_request_of_group(html, groupname)
	OUT = out_week(beautiful_out(content.text))
	return(OUT)


