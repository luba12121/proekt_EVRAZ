# Тема занятия: Веб-парсинг

#1 Установка библиотек
#pip install html
#pip install requests(выполнени запроса)
#pip install beautifulsoup4

#2 подключение библиотек
import requests
from bs4 import BeautifulSoup
base_url = 'https://quotes.toscrape.com/'

#3 Выполнение запроса на  получение страницы
response = requests.get(base_url)
#print(response.text)

# 4 Преобразуем строку с HTML с BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')

#5 Поиск цитат на странице
quotes = soup.find_all('span',class_='text')

#6 Поиск авторов
authors = soup.find_all('small',class_='author')

# 7 Поиск тегов на странице
tags = soup.find_all('div',class_='tags')

for page in range(1,4):
    #print page in range(4)
    print('Страница №' + str(page))
    if page == 1:
        url = base_url
    else:
        url = base_url  + 'page/' + str(page)

    # 3 Выполнение запроса на  получение страницы
    response = requests.get(url)
    # print(response.text)

    # 4 Преобразуем строку с HTML с BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # 5 Поиск цитат на странице
    quotes = soup.find_all('span', class_='text')

    # 6 Поиск авторов
    authors = soup.find_all('small', class_='author')

    # 7 Поиск тегов на странице
    tags = soup.find_all('div', class_='tags')

 # 8 Вывод цитат в консоль
    for i in range(len(quotes)):
        print(quotes[i].text)
        print('--' + authors[i].text)
        #print(tags[i])
        quote_tags = tags[i].find_all('a',class_='tag')
        #print(quote_tags)
        for tag in quote_tags:
            print(tag.text)
        print('\n')

