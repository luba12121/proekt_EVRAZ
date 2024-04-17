# import requests
# from bs4 import BeautifulSoup
# base_url = 'https://realpython.github.io/fake-jobs/'

# response = requests.get(base_url)

# soup = BeautifulSoup(response.text, 'lxml')

# vacans = soup.find_all('h2',class_='title is-5')

# company = soup.find_all('h3',class_='subtitle is-6 company')

# adres = soup.find_all('p',class_='location')Д

# data = soup.find_all('time')

# for i in range(len(vacans)):
#     print('Название вакансии: ' + vacans[i].text)
#     #print('--' + company [i].text)
#     #print(tags[i])
#     #vacans_data  = data [i].find_all('a',class_='tag')
#     print('Компания: ' + company[i].text)
#     print('адрес: ' + adres[i].text.strip())
#     print('дата публикации: ' + data[i].text.strip())
#     #print(quote_tags)
#     # for data  in vacans_data :
#     #     print(data .text)
#     print('\n')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# import requests
# from bs4 import BeautifulSoup
# base_url = 'https://scrapingclub.com/exercise/list_basic/'

# for page in range(1, 7):
#     print('Страница №'+ + str(page))
#     if page == 1:
#         url = base_url
#     else:
#         url = base_url + '?page=' + str(page)

#     print(url)

#     response = requests.get(url)

#     soup = BeautifulSoup(response.text, 'lxml')

#     naswanie = soup.find_all('h4')

#     cena = soup.find_all('h5')



#     for i in range(len(naswanie)):
#         print('Товар: ' + naswanie[i].text.replace('\n', ''))
#         print('цена: ' + cena[i].text.strip())
#         print('\n')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''import requests
from bs4 import BeautifulSoup
base_url = 'https://glavsnab.net/elektrotehnicheskoe-oborudovanie-2/schitovoe-oborudovanie.html'


response = requests.get('https://www.evraz.com/ru/news-and-media/press-releases-and-news/')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    print('Товар: ' + name.text)
    print('Цена: ' + cena[i].text)
    print('\n')'''
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#####11111
import requests
from bs4 import BeautifulSoup
import json
base_url = 'https://glavsnab.net/zimniye-tovary/svetodiodnyye-girlyandy.html'
print('Гирлянды')
response = requests.get('https://glavsnab.net/zimniye-tovary/svetodiodnyye-girlyandy.html')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

products = []

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    products.append({
        'name': name.text,
        'cena': cena[i].text
    })
file = open('svetodiodnyye-girlyandy.json', 'w', encoding='utf-8')
json.dump(products, file, ensure_ascii=False)
file.close()
    # response.close()
######################222222
base_url = 'https://glavsnab.net/zimniye-tovary/svetodiodnyye-figury.html'
print('Светодиодные фигуры')
response = requests.get('https://glavsnab.net/zimniye-tovary/svetodiodnyye-figury.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    products.append({
        'name': name.text,
        'cena': cena[i].text
    })
file = open('svetodiodni-figuri.json', 'w', encoding='utf-8')
json.dump(products, file, ensure_ascii=False)
file.close()

#######################3333333333

base_url = 'https://glavsnab.net/tovary-dlya-doma/dekor-dlya-doma-2/shtory-karnizy-zhalyuzi.html'
print('Шторы, Карнизы, жалюза')
response = requests.get('https://glavsnab.net/tovary-dlya-doma/dekor-dlya-doma-2/shtory-karnizy-zhalyuzi.html')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    products.append({
        'name': name.text,
        'cena': cena[i].text
    })
    file = open('shtora-carniza-salqza.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
##########################################44444444

base_url = 'https://glavsnab.net/krovlya-fasad-zabor/listovyye-plastiki/monolitnyy.html'
print('поликорбанат')
response = requests.get('https://glavsnab.net/krovlya-fasad-zabor/listovyye-plastiki/monolitnyy.html')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    products.append({
        'name': name.text,
        'cena': cena[i].text
    })
    file = open('polikarbonat.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
################################################55555555555

base_url = 'https://glavsnab.net/krepezh-1/samorezi.html'
print('Саморезы')
response = requests.get('https://glavsnab.net/krepezh-1/samorezi.html')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    products.append({
        'name': name.text,
        'cena': cena[i].text
    })
    file = open('samores.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()

######################66666666666

base_url = 'https://glavsnab.net/krepezh-1/shurupi.html'
print('шурупы')
response = requests.get('https://glavsnab.net/krepezh-1/shurupi.html')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    print('Товар: ' + name.text)
    print('Цена: ' + cena[i].text)
    print('\n')
    file = open('shurup.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
######################77777777777
base_url = 'https://glavsnab.net/krepezh-1/gayki.html'
print('гайки')
response = requests.get('https://glavsnab.net/krepezh-1/gayki.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    title = name.find('a')
    price = cards[i].find('span', class_='num')
    if price is None:
        price = cards[i].find('span', class_='price-new')
    print('Товар: ' + title.text)
    print('Цена: ' + price.text)
    print('\n')
    file = open('gayki.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()

######################################8888888
base_url = 'https://glavsnab.net/instrument-i-oborudovaniye/benzopily/benzopily-bytovyye.html'
print('бензопилы')
response = requests.get('https://glavsnab.net/instrument-i-oborudovaniye/benzopily/benzopily-bytovyye.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    title = name.find('a')
    price = cards[i].find('span', class_='num')
    if price is None:
        price = cards[i].find('span', class_='price-new')
    print('Товар: ' + title.text)
    print('Цена: ' + price.text)
    print('\n')
    file = open('benzopils.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
###################9999999999999999

base_url = 'https://glavsnab.net/zimniye-tovary/zimniye-peny.html'
print('Зимние пены')
response = requests.get('https://glavsnab.net/zimniye-tovary/zimniye-peny.html')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    print('Товар: ' + name.text)
    print('Цена: ' + cena[i].text)
    print('\n')
    file = open('zimnipens.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
##########################10

base_url = 'https://glavsnab.net/izolyatsiya/geomembrany/profilirovannyye-membrany.html'
print('геомембраны')
response = requests.get('https://glavsnab.net/izolyatsiya/geomembrany/profilirovannyye-membrany.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    title = name.find('a')
    price = cards[i].find('span', class_='num')
    if price is None:
        price = cards[i].find('span', class_='price-new')
    print('Товар: ' + title.text)
    print('Цена: ' + price.text)
    print('\n')
    file = open('geomembrans.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
    #######################11


base_url = 'https://glavsnab.net/zimniye-tovary/snegovyye-lopaty.html'
print('Лопаты')
response = requests.get('https://glavsnab.net/zimniye-tovary/snegovyye-lopaty.html')
soup = BeautifulSoup(response.text, 'lxml')

nasvanye = soup.find_all('div',class_='product-card__name')

cena = soup.find_all('span',class_='num')

for i in range(len(nasvanye)):
    name = nasvanye[i].find('a')
    print('Товар: ' + name.text)
    print('Цена: ' + cena[i].text)
    print('\n')
    file = open('lopats.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
########################12
base_url = 'https://glavsnab.net/stroymateriali/kirpich/stroitelnyy-kirpich.html'
print('кирпич')
response = requests.get('https://glavsnab.net/stroymateriali/kirpich/stroitelnyy-kirpich.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    title = name.find('a')
    price = cards[i].find('span', class_='num')
    if price is None:
        price = cards[i].find('span', class_='price-new')
    print('Товар: ' + title.text)
    print('Цена: ' + price.text)
    print('\n')
    file = open('kirpich.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
##########################13

base_url = 'https://glavsnab.net/otdelochnie-materiali/oboi/bumazhnie-oboi.html'
print('Обои')
response = requests.get('https://glavsnab.net/otdelochnie-materiali/oboi/bumazhnie-oboi.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    title = name.find('a')
    price = cards[i].find('span', class_='num')
    if price is None:
        price = cards[i].find('span', class_='price-new')
    print('Товар: ' + title.text)
    print('Цена: ' + price.text)
    print('\n')
    file = open('oboi.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
####################14
base_url = 'https://glavsnab.net/otdelochnie-materiali/stenovyye-paneli/paneli-pvkh.html'
print('Панели')
response = requests.get('https://glavsnab.net/otdelochnie-materiali/stenovyye-paneli/paneli-pvkh.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    title = name.find('a')
    price = cards[i].find('span', class_='num')
    if price is None:
        price = cards[i].find('span', class_='price-new')
    print('Товар: ' + title.text)
    print('Цена: ' + price.text)
    print('\n')
    file = open('gayki.json', 'w+', encoding='utf-8')
    json.dump(products, file, ensure_ascii=False)
    file.close()
####################15
base_url = 'https://glavsnab.net/izolyatsiya/teploizolyaciya/penoplast.html'
print('Пинопласт')
response = requests.get('https://glavsnab.net/izolyatsiya/teploizolyaciya/penoplast.html')
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div',class_='product-card')


for i in range(len(cards)):
    name = cards[i].find('div', class_='product-card__name')
    title = name.find('a')
    price = cards[i].find('span', class_='num')
    if price is None:
        price = cards[i].find('span', class_='price-new')
    print('Товар: ' + title.text)
    print('Цена: ' + price.text)
    print('\n')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#pip install pyTelegramBotAPI
import telebot
from telebot import types

token = '7079430072:AAFpL3abe5EIpp2kfqgnu5GwWkn_81sldrM'

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == '/start':
        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'начать работу с ботом'),
                types.BotCommand('/dance', 'Милый стикер')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='светодиодные фигуры', callback_data='Cветодиодные фигуры')
        keyboard.add(button1)
        button2 = types.InlineKeyboardButton(text='Гирлянды', callback_data='гирлянды')
        keyboard.add(button2)
        button3 = types.InlineKeyboardButton(text='Шторы', callback_data='Шторы')
        keyboard.add(button3)
        button4 = types.InlineKeyboardButton(text='Поликарбонат', callback_data='поликарбонат')
        keyboard.add(button4)
        button5 = types.InlineKeyboardButton(text='Саморезы', callback_data='саморезы')
        keyboard.add(button5)
        button6 = types.InlineKeyboardButton(text='Шурупы', callback_data='шурупы')
        keyboard.add(button6)
        button7 = types.InlineKeyboardButton(text='Гайки', callback_data='гайки')
        keyboard.add(button7)
        button8 = types.InlineKeyboardButton(text='Бензопилы', callback_data='безопилы')
        keyboard.add(button8)
        button9 = types.InlineKeyboardButton(text='Зимние пены', callback_data='зимние пены')
        keyboard.add(button9)
        button10 = types.InlineKeyboardButton(text='Геомембраны', callback_data='геомембраны')
        keyboard.add(button10)
        button11 = types.InlineKeyboardButton(text='Лопаты', callback_data='лопаты')
        keyboard.add(button11)
        button12 = types.InlineKeyboardButton(text='Кирпич', callback_data='кирпич')
        keyboard.add(button12)
        button13 = types.InlineKeyboardButton(text='Обои', callback_data='обои')
        keyboard.add(button13)
        button14 = types.InlineKeyboardButton(text='Панели', callback_data='панели')
        keyboard.add(button14)
        button15 = types.InlineKeyboardButton(text='Пиноплат', callback_data='пинопласт')
        keyboard.add(button15)
        bot.send_message(message.from_user.id,
                         text='Приветствуем в Суслик Строй! Мы рады вас видеть это не бобер строй это СУСЛИК СТРОЙ')
        bot.send_message(message.from_user.id,
                         text='Выберите одну из категории товаров', reply_markup=keyboard)
    elif message.text == '/dance':
            bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAELduBl1grGWvU2pWGNsUz8sN2dp0b8qwAC_EYAAs1wGUvljyFbpxP0kDQE')
#print(message.from_user.id)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        bot.send_message(call.from_user.id, text='Вы нажали на кнопку - ' + call.data)
        if call.data == 'Cветодиодные фигуры':
            file = open('svetodiodni-figuri.json', 'r+', encoding='utf-8')
            products = json.load(file)
            file.close()
            text = 'товары из категории: *Световые фигуры*\n\n'
            for product in products[:10]:
                text += '*Название:* ' + product['name'] + '\n.'
                text += '*цена:* ' + product['cena'] + '\n.'
            bot.send_message(call.from_user.id,text=text, parse_mode = 'Markdown')
        print(call.data)



bot.polling(none_stop=True, interval=0)



































































































#                      *************
#                   *************
# #                     |   |
# #                     |   |
# #         =========================
# #      =================================
# # ======= """""""""""""""""""""""""""=======
# #         |                         |
# #         |    |--------------      |
# #         |    |             |      |
# #         |    |             |      |
# #         |    |             |      |
# #         |    |             |      |
# #         |    |--------------      |
# #         |                         |
# #         """""""""""""""""""""""""'    Артем с днем Свежего Ананаса мы дарим вам дом!
#                                         Дом Артема бесплатно, с камином по скидке


