import requests
from bs4 import BeautifulSoup
base_url = 'https://realpython.github.io/fake-jobs/'

response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'lxml')

vacans = soup.find_all('h2',class_='title is-5')

company = soup.find_all('h3',class_='subtitle is-6 company')

adres = soup.find_all('p',class_='location')

data = soup.find_all('time')

for i in range(len(vacans)):
    print('Название вакансии: ' + vacans[i].text)
    #print('--' + company [i].text)
    #print(tags[i])
    #vacans_data  = data [i].find_all('a',class_='tag')
    print('Компания: ' + company[i].text)
    print('адрес: ' + adres[i].text.strip())
    print('дата публикации: ' + data[i].text.strip())
    #print(quote_tags)
    # for data  in vacans_data :
    #     print(data .text)
    print('\n')
