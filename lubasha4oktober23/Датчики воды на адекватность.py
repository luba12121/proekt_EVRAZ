import json
from datetime import date
from datetime import datetime, timedelta
file = open('cex1.json', 'w+', encoding='utf-8')
cex1 = {
    "cex": 1,
    "datchik1": 1.1,
    "datchik2": 2.1,
    "datchik3": 3.1,
    "datchik4": 4.1
}
json.dump(cex1, file, ensure_ascii=False)
file.close()

ddd=''

def get_date(message):
    global ddd
    print(message.text)
    ddd = str(message.text)
    file = open('datchik1.1.json', 'r', encoding='utf-8')
    dannie = json.load(file)
    spisokdata = []
    for i in range(len(dannie)):
        if ddd == dannie[i]['date']:
            spisokdata.append(dannie[i])
    print(spisokdata)
    text1 = ''
    for i in range(len(spisokdata)):
        text1 += '*название цеха*: ' + str(spisokdata[i]['cex']) + '\n'
        text1 += '*№ датчика*: ' + str(spisokdata[i]['datchik']) + '\n'
        text1 += '*дата*: ' + str(spisokdata[i]['date']) + '\n'
        text1 += '*Температура воды*: ' + str(spisokdata[i]['znachenie']) + '\n'
        if spisokdata[i]['znachenie'] > 99:
            text1 += '\n*!!!Аномальные показатели на датчике!!!*\n'
    bot.send_message(message.from_user.id, text = text1, parse_mode='Markdown')


    file.close()


#Первый датчик ЦЕХ 1
file = open('datchik1.1.json', 'w+', encoding='utf-8')
today = date.today()
yesterday =  today - timedelta(days = 1)
# week = (today - timedelta(days = 1)) + (today - timedelta(days = 2)) + (today - timedelta(days = 3)) + (today - timedelta(days = 4)) + (today - timedelta(days = 5)) + (today - timedelta(days = 6)) + (today - timedelta(days = 7))
week = (today - timedelta(days = 7))
week2 = (today - timedelta(days = 6))
week3 = (today - timedelta(days = 5))
week4 = (today - timedelta(days = 4))
week5 = (today - timedelta(days = 3))
week6 = (today - timedelta(days = 2))
week7 = (today - timedelta(days = 1))
datchik1 = [{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(today),
    "znachenie": 100
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(yesterday),
    "znachenie": 55
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(week),
    "znachenie": 54
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(week2),
    "znachenie": 14
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(week3),
    "znachenie": 67
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(week4),
    "znachenie": 78
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(week5),
    "znachenie": 81
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(week6),
    "znachenie": 74
},
{
    "cex": "цех химического улавливания",
    "datchik": 1.1,
    "date": str(week7),
    "znachenie": 42
},
# {
#     "cex": "цех химического улавливания",
#     "datchik": 1.1,
#     "date": str(ddd),
#     "znachenie": 77
# }
]
json.dump(datchik1, file, ensure_ascii=False)
file.close()
#Второй датчик ЦЕХ 1
file = open('datchik2.1.json', 'w+', encoding='utf-8')
datchik2 = [{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": "2024-02-28",
    "znachenie": 25
  }]
json.dump(datchik2, file, ensure_ascii=False)
file.close()
#Третий датчик ЦЕХ 1
file = open('datchik3.1.json', 'w+', encoding='utf-8')
datchik3 = [{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": "2024-02-28",
    "znachenie": 28
  }]
json.dump(datchik3, file, ensure_ascii=False)
file.close()
#Четвертый датчик ЦЕХ 1
file = open('datchik4.1.json', 'w+', encoding='utf-8')
datchik4 = [{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": "2024-02-28",
    "znachenie": 17
  }]
json.dump(datchik4, file, ensure_ascii=False)
file.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import json
file = open('cex2.json', 'w+', encoding='utf-8')
cex2 = {
    "cex": "смолоперерабатывающий цех",
    "datchik1": 1.2,
    "datchik2": 2.2,
    "datchik3": 3.2,
    "datchik4": 4.2
}
json.dump(cex2, file, ensure_ascii=False)
file.close()

#Первый датчик ЦЕХ 2
file = open('datchik1.2.json', 'w+', encoding='utf-8')
datchik1 = [{
    "cex": "смолоперерабатывающий цех",
    "datchik": 1.2,
    "date": "2024-02-28",
    "znachenie": 45
}]
json.dump(datchik1, file, ensure_ascii=False)
file.close()
#Второй датчик ЦЕХ 2
file = open('datchik2.2.json', 'w+', encoding='utf-8')
datchik2 = [{
    "cex": "смолоперерабатывающий цех",
    "datchik": 2.2,
    "date": "2024-02-28",
    "znachenie": 33
  }]
json.dump(datchik2, file, ensure_ascii=False)
file.close()
#Третий датчик ЦЕХ 2
file = open('datchik3.2.json', 'w+', encoding='utf-8')
datchik3 = [{
    "cex": "смолоперерабатывающий цех",
    "datchik": 3.2,
    "date": "2024-02-28",
    "znachenie": 177
  }]
json.dump(datchik3, file, ensure_ascii=False)
file.close()
#Четвертый датчик ЦЕХ 2
file = open('datchik4.2.json', 'w+', encoding='utf-8')
datchik4 = [{
    "cex": "смолоперерабатывающий цех",
    "datchik": 4.2,
    "date": "2024-02-28",
    "znachenie": 21
  }]
json.dump(datchik4, file, ensure_ascii=False)
file.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import json
file = open('cex3.json', 'w+', encoding='utf-8')
cex2 = {
    "cex": "углеподготовительный цех",
    "datchik1": 1.3,
    "datchik2": 2.3,
    "datchik3": 3.3,
    "datchik4": 4.3
}
json.dump(cex2, file, ensure_ascii=False)
file.close()

#Первый датчик ЦЕХ 3
file = open('datchik1.3.json', 'w+', encoding='utf-8')
datchik1 = [{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": "2024-02-28",
    "znachenie": 14
}]
json.dump(datchik1, file, ensure_ascii=False)
file.close()
#Второй датчик ЦЕХ 3
file = open('datchik2.3.json', 'w+', encoding='utf-8')
datchik2 = [{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": "2024-02-28",
    "znachenie": 74
  }]
json.dump(datchik2, file, ensure_ascii=False)
file.close()
#Третий датчик ЦЕХ 3
file = open('datchik3.3.json', 'w+', encoding='utf-8')
datchik3 = [{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": "2024-02-28",
    "znachenie": 22
  }]
json.dump(datchik3, file, ensure_ascii=False)
file.close()
#Четвертый датчик ЦЕХ 3
file = open('datchik4.3.json', 'w+', encoding='utf-8')
datchik4 = [{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": "2024-02-28",
    "znachenie": 82
  }]
json.dump(datchik4, file, ensure_ascii=False)
file.close()

import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

token = '6644060607:AAGkixM7ItktRc2ZJLjOhXZsuOKnuji6vlc'

 # def get_date(message):
 #     print(message.text)
 #     poldata = str(message.text)

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == '/start':
        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'начать работу с ботом')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )

        bot.send_message(message.from_user.id,
                         text='Здравствуйте!Начнем анализировать показания датчиков...')

        keyboard = types.InlineKeyboardMarkup()
        button10 = types.InlineKeyboardButton(text='цех химического улавливания', callback_data='цех химического улавливания')
        keyboard.add(button10)
        button20 = types.InlineKeyboardButton(text='смолоперерабатывающий цех', callback_data='смолоперерабатывающий цех')
        keyboard.add(button20)
        button30 = types.InlineKeyboardButton(text='углеподготовительный цех',callback_data='углеподготовительный цех')
        keyboard.add(button30)

        bot.send_message(message.from_user.id,
                         text='проверяем датчики...')
        bot.send_message(message.from_user.id,
                         text='Выберите однин из цехов', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global today

    file = open('cex1.json', 'r+', encoding='utf-8')
    products = json.load(file)
    file.close()

    if call.data == 'цех химического улавливания':
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        file = open('datchik1.json', 'r+', encoding='utf-8')
        products = json.load(file)
        file.close()
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Датчик 1.1', callback_data='Датчик 1.1')
        keyboard.add(button1)
        button2 = types.InlineKeyboardButton(text='Датчик 2.1', callback_data='Датчик 2.1')
        keyboard.add(button2)
        button3 = types.InlineKeyboardButton(text='Датчик 3.1', callback_data='Датчик 3.1')
        keyboard.add(button3)
        button4 = types.InlineKeyboardButton(text='Датчик 4.1', callback_data='Датчик 4.1')
        keyboard.add(button4)
        bot.send_message(call.from_user.id,
                         text='Выберите один из датчиков', reply_markup=keyboard)
    # text = 'у датчика' + str(products['datchik']) + 'Недопустимые значения\n\n'
    if call.data == 'Датчик 1.1':
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button11 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button11)
        button22 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22)
        button33 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button33)
        button44 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button44)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний',reply_markup=keyboard)
    if call.data == 'показания сегодня':
        file = open('datchik1.1.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        datchik_today = []
        for pokazanie in data:
            if pokazanie['date'] == str(today):
                datchik_today.append(pokazanie)

        text = '*Результаты пeрвого датчика за сегодня*\n\n'
        for i in range(len(datchik_today)):
            text += '*название цеха*: ' + str(datchik_today[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(datchik_today[i]['datchik']) + '\n'
            text += '*дата*: ' + str(datchik_today[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(datchik_today[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*\n'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        today = date.today()
        print("Today date is: ", today)

    if ddd == str(today):
        datchik_today.append(pokazanie)

        text = '*Результаты пeрвого датчика за сегодня*\n\n'
        for i in range(len(datchik_today)):
            text += '*название цеха*: ' + str(datchik_today[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(datchik_today[i]['datchik']) + '\n'
            text += '*дата*: ' + str(datchik_today[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(datchik_today[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*\n'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        today = date.today()
        print("Today date is: ", today)


    elif call.data == 'показания вчера':
        file = open('datchik1.1.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        datchik_yesterday = []
        for pokazanie in data:
            if pokazanie['date'] == str(yesterday):
                datchik_yesterday.append(pokazanie)
        print(datchik_yesterday)
        text = '*Результаты пeрвого датчика за вчера*\n\n'
        for i in range(len(datchik_yesterday)):
            text += '*название цеха*: ' + str(datchik_yesterday[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(datchik_yesterday[i]['datchik']) + '\n'
            text += '*дата*: ' + str(datchik_yesterday[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(datchik_yesterday[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*\n'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        today = date.today()
        print("Yesterday date is: ", yesterday)

    elif call.data == 'показания недели':
        file = open('datchik1.1.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        datchik_week = []
        for pokazanie in data:
            #if pokazanie['date'] < today and pokazanie['date']> week:
            pokazanie_date = datetime.strptime(pokazanie['date'], '%Y-%m-%d')
            pokazanie_date = datetime.date(pokazanie_date)
            # data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

            if today >= pokazanie_date >= week:
                datchik_week.append(pokazanie)
                print(datchik_week)
        text = '*Результаты пeрвого датчика за неделю*\n\n'

        for i in range(len(datchik_week)):
            text += '*название цеха*: ' + str(datchik_week[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(datchik_week[i]['datchik']) + '\n'
            text += '*дата*: ' + str(datchik_week[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(datchik_week[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*\n'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        today = date.today()

        print(products)

    elif call.data == 'выбрать свою дату':
        textpol = '*Напишите дату за которую нужно узнать показания*'
        bot.send_message(call.from_user.id, text=textpol, parse_mode='Markdown')
        bot.register_next_step_handler(call.message, get_date)
        # znach = []
        # znach.append(messages.to_dict())

    if call.data == 'Датчик 2.1':
        file = open('datchik2.1.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты второго датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)


    if call.data == 'Датчик 3.1':
        file = open('datchik3.1.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты третьего датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)

    if call.data == 'Датчик 4.1':
        file = open('datchik4.1.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты четвертого датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)

    if call.data == 'смолоперерабатывающий цех':
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        file = open('datchik1.json', 'r+', encoding='utf-8')
        products = json.load(file)
        file.close()
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Датчик 1.2', callback_data='Датчик 1.2')
        keyboard.add(button1)
        button2 = types.InlineKeyboardButton(text='Датчик 2.2', callback_data='Датчик 2.2')
        keyboard.add(button2)
        button3 = types.InlineKeyboardButton(text='Датчик 3.2', callback_data='Датчик 3.2')
        keyboard.add(button3)
        button4 = types.InlineKeyboardButton(text='Датчик 4.2', callback_data='Датчик 4.2')
        keyboard.add(button4)
        bot.send_message(call.from_user.id,
                         text='Выберите один из датчиков', reply_markup=keyboard)
    # text = 'у датчика' + str(products['datchik']) + 'Недопустимые значения\n\n'
    if call.data == 'Датчик 1.2':
        file = open('datchik1.2.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты пeрвого датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')

        print(products)
    #
    if call.data == 'Датчик 2.2':
        file = open('datchik2.2.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты второго датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)


    elif call.data == 'Датчик 3.2':
        file = open('datchik3.2.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты третьего датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)

    if call.data == 'Датчик 4.2':
        file = open('datchik4.2.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты четвертого датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)


    if call.data == 'углеподготовительный цех':
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        file = open('datchik1.json', 'r+', encoding='utf-8')
        products = json.load(file)
        file.close()
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Датчик 1.3', callback_data='Датчик 1.3')
        keyboard.add(button1)
        button2 = types.InlineKeyboardButton(text='Датчик 2.3', callback_data='Датчик 2.3')
        keyboard.add(button2)
        button3 = types.InlineKeyboardButton(text='Датчик 3.3', callback_data='Датчик 3.3')
        keyboard.add(button3)
        button4 = types.InlineKeyboardButton(text='Датчик 4.3', callback_data='Датчик 4.3')
        keyboard.add(button4)
        bot.send_message(call.from_user.id,
                         text='Выберите один из датчиков', reply_markup=keyboard)
    # text = 'у датчика' + str(products['datchik']) + 'Недопустимые значения\n\n'
    if call.data == 'Датчик 1.3':
        file = open('datchik1.3.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты пeрвого датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')


        print(products)
#
    if call.data == 'Датчик 2.3':
        file = open('datchik2.3.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты второго датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)


    if call.data == 'Датчик 3.3':
        file = open('datchik3.3.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты третьего датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)

    if call.data == 'Датчик 4.3':
        file = open('datchik4.3.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        text = '*Результаты четвертого датчика*\n\n'
        for i in range(len(data)):
            text += '*название цеха*: ' + str(data[i]['cex']) + '\n'
            text += '*№ датчика*: ' + str(data[i]['datchik']) + '\n'
            text += '*дата*: ' + str(data[i]['date']) + '\n'
            text += '*Температура воды*: ' + str(data[i]['znachenie']) + '\n'
            if data[i]['znachenie'] > 99:
                text += '\n*!!!Аномальные показатели на датчике!!!*'
        bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
        print(products)

bot.polling(none_stop=True)
