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
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik2 = [{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(today2),
    "znachenie": 11
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(yesterday2),
    "znachenie": 76
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week2),
    "znachenie": 96
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week22),
    "znachenie": 34
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week32),
    "znachenie": 42
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week42),
    "znachenie": 71
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week52),
    "znachenie": 21
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week62),
    "znachenie": 65
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week72),
    "znachenie": 33
},
]
json.dump(datchik2, file, ensure_ascii=False)
file.close()
#Третий датчик ЦЕХ 1
file = open('datchik3.1.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik3 = [{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(today2),
    "znachenie": 23
},
{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(yesterday2),
    "znachenie": 84
},
{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(week2),
    "znachenie": 34
},
{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(week22),
    "znachenie": 56
},
{
    "cex": "цех химического улавливания",
    "datchik": 2.1,
    "date": str(week32),
    "znachenie": 21
},
{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(week42),
    "znachenie": 98
},
{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(week52),
    "znachenie": 123
},
{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(week62),
    "znachenie": 45
},
{
    "cex": "цех химического улавливания",
    "datchik": 3.1,
    "date": str(week72),
    "znachenie": 99
},
]
json.dump(datchik3, file, ensure_ascii=False)
file.close()

# четвертый датчик цех 1
file = open('datchik4.1.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik4 = [{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(today2),
    "znachenie": 66
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(yesterday2),
    "znachenie": 54
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(week2),
    "znachenie": 12
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(week22),
    "znachenie": 92
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(week32),
    "znachenie": 45
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(week42),
    "znachenie": 27
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(week52),
    "znachenie": 555
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(week62),
    "znachenie": 61
},
{
    "cex": "цех химического улавливания",
    "datchik": 4.1,
    "date": str(week72),
    "znachenie": 73
},
]
json.dump(datchik4, file, ensure_ascii=False)
file.close()

#Первый датчик ЦЕХ 2
file = open('datchik1.2.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik1 = [{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(today2),
    "znachenie": 76
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(yesterday2),
    "znachenie": 234
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(week2),
    "znachenie": 39
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(week22),
    "znachenie": 21
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(week32),
    "znachenie": 74
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(week42),
    "znachenie": 52
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(week52),
    "znachenie": 23
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(week62),
    "znachenie": 78
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.2,
    "date": str(week72),
    "znachenie": 51
},
]
json.dump(datchik1, file, ensure_ascii=False)
file.close()

#второй датчик ЦЕХ 2
file = open('datchik2.2.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik2 = [{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(today2),
    "znachenie": 97
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(yesterday2),
    "znachenie": 52
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(week2),
    "znachenie": 77
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(week22),
    "znachenie": 67
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(week32),
    "znachenie": 68
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(week42),
    "znachenie": 65
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(week52),
    "znachenie": 22
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(week62),
    "znachenie": 15
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.2,
    "date": str(week72),
    "znachenie": 41
},
]
json.dump(datchik2, file, ensure_ascii=False)
file.close()

#третий датчик ЦЕХ 2
file = open('datchik3.2.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik3 = [{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(today2),
    "znachenie": 999
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(yesterday2),
    "znachenie": 54
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(week2),
    "znachenie": 26
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(week22),
    "znachenie": 93
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(week32),
    "znachenie": 54
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(week42),
    "znachenie": 25
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(week52),
    "znachenie": 76
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(week62),
    "znachenie": 22
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.2,
    "date": str(week72),
    "znachenie": 90
},
]
json.dump(datchik3, file, ensure_ascii=False)
file.close()

#Четвертый датчик ЦЕХ 2
file = open('datchik4.2.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik4 = [{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(today2),
    "znachenie": 76
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(yesterday2),
    "znachenie": 234
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(week2),
    "znachenie": 39
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(week22),
    "znachenie": 21
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(week32),
    "znachenie": 74
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(week42),
    "znachenie": 52
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(week52),
    "znachenie": 23
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(week62),
    "znachenie": 78
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.2,
    "date": str(week72),
    "znachenie": 51
},
]
print(1234)
json.dump(datchik4, file, ensure_ascii=False)
file.close()

#первый длатчик ЦЕХ 3
file = open('datchik1.3.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik1 = [{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(today2),
    "znachenie": 30
},
{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(yesterday2),
    "znachenie": 59
},
{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(week2),
    "znachenie": 44
},
{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(week22),
    "znachenie": 91
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 1.3,
    "date": str(week32),
    "znachenie": 83
},
{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(week42),
    "znachenie": 109
},
{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(week52),
    "znachenie": 51
},
{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(week62),
    "znachenie": 18
},
{
    "cex": "углеподготовительный цех",
    "datchik": 1.3,
    "date": str(week72),
    "znachenie": 101
},
]
json.dump(datchik1, file, ensure_ascii=False)
file.close()

#второй датчик ЦЕХ 3
file = open('datchik2.3.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik2 = [{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(today2),
    "znachenie": 7
},
{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(yesterday2),
    "znachenie": 41
},
{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(week2),
    "znachenie": 51
},
{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(week22),
    "znachenie": 87
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 2.3,
    "date": str(week32),
    "znachenie": 15
},
{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(week42),
    "znachenie": 55
},
{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(week52),
    "znachenie": 80
},
{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(week62),
    "znachenie": 52
},
{
    "cex": "углеподготовительный цех",
    "datchik": 2.3,
    "date": str(week72),
    "znachenie": 17
},
]
json.dump(datchik2, file, ensure_ascii=False)
file.close()

# Третий датчик ЦЕХ 3
file = open('datchik3.3.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik3 = [{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(today2),
    "znachenie": 109
},
{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(yesterday2),
    "znachenie": 5
},
{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(week2),
    "znachenie": 20
},
{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(week22),
    "znachenie": 73
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 3.3,
    "date": str(week32),
    "znachenie": 72
},
{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(week42),
    "znachenie": 54
},
{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(week52),
    "znachenie": 48
},
{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(week62),
    "znachenie": 82
},
{
    "cex": "углеподготовительный цех",
    "datchik": 3.3,
    "date": str(week72),
    "znachenie": 45
},
]
json.dump(datchik3, file, ensure_ascii=False)
file.close()

#Четвертый датчик ЦЕХ 3
file = open('datchik4.3.json', 'w+', encoding='utf-8')
today2 = date.today()
yesterday2 =  today - timedelta(days = 1)
week22 = (today - timedelta(days = 6))
week32 = (today - timedelta(days = 5))
week42 = (today - timedelta(days = 4))
week52 = (today - timedelta(days = 3))
week62 = (today - timedelta(days = 2))
week72 = (today - timedelta(days = 1))
datchik4 = [{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(today2),
    "znachenie": 19
},
{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(yesterday2),
    "znachenie": 67
},
{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(week2),
    "znachenie": 93
},
{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(week22),
    "znachenie": 44
},
{
    "cex": "смолеперерабатывающий цех",
    "datchik": 4.3,
    "date": str(week32),
    "znachenie": 98
},
{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(week42),
    "znachenie": 66
},
{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(week52),
    "znachenie": 34
},
{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(week62),
    "znachenie": 2
},
{
    "cex": "углеподготовительный цех",
    "datchik": 4.3,
    "date": str(week72),
    "znachenie": 10
},
]
json.dump(datchik4, file, ensure_ascii=False)
file.close()

import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

token = '6644060607:AAGkixM7ItktRc2ZJLjOhXZsuOKnuji6vlc'

active_datchik = 0

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
    global today, active_datchik

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
        active_datchik = call.data
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
        file_name = ''
        if active_datchik == 'Датчик 1.1':
            file_name = 'datchik1.1.json'
        elif active_datchik == 'Датчик 2.1':
            file_name = 'datchik2.1.json'
        elif active_datchik == 'Датчик 3.1':
            file_name = 'datchik3.1.json'
        elif active_datchik == 'Датчик 4.1':
            file_name = 'datchik4.1.json'
        elif active_datchik == 'Датчик 1.2':
            file_name = 'datchik1.2.json'
        elif active_datchik == 'Датчик 2.2':
            file_name = 'datchik2.2.json'
        elif active_datchik == 'Датчик 3.2':
            file_name = 'datchik3.2.json'
        elif active_datchik == 'Датчик 4.2':
            file_name = 'datchik4.2.json'
        elif active_datchik == 'Датчик 1.3':
            file_name = 'datchik1.3.json'
        elif active_datchik == 'Датчик 2.3':
            file_name = 'datchik2.3.json'
        elif active_datchik == 'Датчик 3.3':
            file_name = 'datchik3.3.json'
        elif active_datchik == 'Датчик 4.3':
            file_name = 'datchik4.3.json'

        print(file_name)
        file = open(file_name, 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        datchik_today = []
        for pokazanie in data:
            if pokazanie['date'] == str(today):
                datchik_today.append(pokazanie)

        text = '*Результаты  датчика за сегодня*\n\n'
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
        file_name = ''
        if active_datchik == 'Датчик 1.1':
            file_name = 'datchik1.1.json'
        elif active_datchik == 'Датчик 2.1':
            file_name = 'datchik2.1.json'
        elif active_datchik == 'Датчик 3.1':
            file_name = 'datchik3.1.json'
        elif active_datchik == 'Датчик 4.1':
            file_name = 'datchik4.1.json'
        elif active_datchik == 'Датчик 1.2':
            file_name = 'datchik1.2.json'
        elif active_datchik == 'Датчик 2.2':
            file_name = 'datchik2.2.json'
        elif active_datchik == 'Датчик 3.2':
            file_name = 'datchik3.2.json'
        elif active_datchik == 'Датчик 4.2':
            file_name = 'datchik4.2.json'
        elif active_datchik == 'Датчик 1.3':
            file_name = 'datchik1.3.json'
        elif active_datchik == 'Датчик 2.3':
            file_name = 'datchik2.3.json'
        elif active_datchik == 'Датчик 3.3':
            file_name = 'datchik3.3.json'
        elif active_datchik == 'Датчик 4.3':
            file_name = 'datchik4.3.json'

        print(file_name)
        file = open(file_name, 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        datchik_yesterday = []
        for pokazanie in data:
            if pokazanie['date'] == str(yesterday):
                datchik_yesterday.append(pokazanie)
        print(datchik_yesterday)
        text = '*Результаты датчика за вчера*\n\n'
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
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button111 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button111)
        button222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button222)
        button333 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button333)
        button444 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button444)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik2.1.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today2 = []
            for pokazanie in data:
                if pokazanie['date'] == str(today2):
                    datchik_today2.append(pokazanie)

        if ddd == str(today2):
            datchik_today2.append(pokazanie)

            text = '*Результаты второго датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)
##########################################################################################################################################################################

    if call.data == 'Датчик 3.1':
        active_datchik = call.data

        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button111 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button111)
        button222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button222)
        button333 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button333)
        button444 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button444)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik3.1.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты третьего датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)

        elif call.data == 'показания вчера':
            file = open('datchik3.1.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_yesterday = []
            for pokazanie in data:
                if pokazanie['date'] == str(yesterday):
                    datchik_yesterday.append(pokazanie)
            print(datchik_yesterday)
            text = '*Результаты третьего датчика за вчера*\n\n'
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

    if call.data == 'Датчик 4.1':
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button1111 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button1111)
        button2222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button2222)
        button3333 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button3333)
        button4444 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button4444)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik4.1.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты четвертого датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)

        elif call.data == 'показания вчера':
            file = open('datchik4.1.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_yesterday = []
            for pokazanie in data:
                if pokazanie['date'] == str(yesterday):
                    datchik_yesterday.append(pokazanie)
            print(datchik_yesterday)
            text = '*Результаты четвертогор датчика за вчера*\n\n'
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
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik1.2.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты первого датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)
    #
    if call.data == 'Датчик 2.2':
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik2.2.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты второго датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)


    elif call.data == 'Датчик 3.2':
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik3.2.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты третьего датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)

    if call.data == 'Датчик 4.2':
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik4.2.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты четвертого датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)


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
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik1.3.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты первого датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)
#
    if call.data == 'Датчик 2.3':
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik2.3.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты второго датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)


    if call.data == 'Датчик 3.3':
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik3.3.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты третьего датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)

    if call.data == 'Датчик 4.3':
        active_datchik = call.data
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        keyboard = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='показания сегодня', callback_data='показания сегодня')
        keyboard.add(button12)
        button22222 = types.InlineKeyboardButton(text='показания вчера', callback_data='показания вчера')
        keyboard.add(button22222)
        button32 = types.InlineKeyboardButton(text='показания недели', callback_data='показания недели')
        keyboard.add(button32)
        button442 = types.InlineKeyboardButton(text='выбрать свою дату', callback_data='выбрать свою дату')
        keyboard.add(button442)
        bot.send_message(call.from_user.id, text='выберите период прсмора показаний', reply_markup=keyboard)
        ###############################################################################################################################################################
        if call.data == 'показания сегодня':
            file = open('datchik4.3.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchik_today = []
            for pokazanie in data:
                if pokazanie['date'] == str(today):
                    datchik_today.append(pokazanie)

        if ddd == str(today):
            datchik_today2.append(pokazanie)

            text = '*Результаты четвертого датчика за сегодня*\n\n'
            for i in range(len(datchik_today2)):
                text += '*название цеха*: ' + str(datchik_today2[i]['cex']) + '\n'
                text += '*№ датчика*: ' + str(datchik_today2[i]['datchik']) + '\n'
                text += '*дата*: ' + str(datchik_today2[i]['date']) + '\n'
                text += '*Температура воды*: ' + str(datchik_today2[i]['znachenie']) + '\n'
                if data[i]['znachenie'] > 99:
                    text += '\n*!!!Аномальные показатели на датчике!!!*\n'
            bot.send_message(call.from_user.id, text=text, parse_mode='Markdown')
            today = date.today()
            print("Today date is: ", today)

bot.polling(none_stop=True)
