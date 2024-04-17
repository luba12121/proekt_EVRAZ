# Выполнение запроса к сервису Dadata
import requests
import json
response = requests.post(
    'http://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
    data=json.dumps({
        "query": '7728551510',
    }),
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Token ba0235c4d6ba3983024e60f0b3143eddf61513a8'
    }
)

print(response.json())
#Запись JSON в файл

#1 json.dump() - из JSON в строку
company = response.json ()
company = company['suggestions'][0]
print(company)
companies = []
companies.append({
    "value": company["value"],
    "inn": company['data']['inn'],
    "ogrn": company['data']['ogrn']

})

file = open('company.json','w',encoding = 'utf-8')
#Запись JSON в файл
json.dump(companies,file,ensure_ascii=False)
file.close()

#Чтение JSON файла

file = open('company.json','r',encoding = 'utf-8')

companies = json.load(file)

print(companies)

#ИНН - Идентификационный номер налогоплательщика
while True:
    print("выберите одно из перечисленных действий:")
    print("1 Поиск организации")
    print("2 просмотр моих организаций")
    print("3 удалить организацию")
    print("4 выход")
    answer = int(input("Введите номер команды"))
    if answer  == 1:
        print("Введите номер организации")
        inn = int(input())
        if inn>99999999999:
            print("Такого кода быть не может")

