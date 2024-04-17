'''''  # Выполнение запроса к сервису Dadata
import requests
import json

response = requests.post(
    'http://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
    data=json.dumps({
        "query": '7728551510',
    }),
    headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Token ba0235c4d6ba3983024e60f0b3143eddf61513a8'
    }
)

print(response.json())
# Запись JSON в файл

# 1 json.dump() - из JSON в строку
company = response.json()
company = company['suggestions'][0]
print(company)
companies = []
companies.append({
    "value": company["value"],
    "inn": company['data']['inn'],
    "ogrn": company['data']['ogrn']

})

file = open('company.json', 'w', encoding='utf-8')
# Запись JSON в файл
json.dump(companies, file, ensure_ascii=False)
file.close()

# Чтение JSON файла

file = open('company.json', 'r', encoding='utf-8')

companies = json.load(file)

print(companies)


#ИНН - Идентификационный номер налогоплательщика '''
#1 
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
        if inn > 999999999999:
            print('Слишком много символов')

        import requests
        import json
        response = requests.post(
            'http://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
            data=json.dumps({
                "query": inn,
            }),
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Token ba0235c4d6ba3983024e60f0b3143eddf61513a8'
            }
        )
        print(response.json())
        print("Хотите ли вы сохранить компанию?")
        otvet = input()
        if otvet == 'да':
            company = response.json ()
            company = company['suggestions'][0]
            file = open('company.json', 'r', encoding='utf-8')
            if len(file.readlines()) == 0:
                companies = []
            else:
                file.seek(0)
                companies = json.load(file)
            file.close()
            print(company)
            companies.append({
                "value": company["value"],
                "inn": company['data']['inn'],
                "ogrn": company['data']['ogrn']
            })
            file = open('company.json', 'w', encoding='utf-8')
            json.dump(companies, file, ensure_ascii=False)
            file.close()
        if otvet == 'нет':
            print('Данная компания не сохранена')

    #2
    elif answer == 2:
        print(companies)
    #3
    elif answer == 3:
        print('введите ИНН компании которую нужно удалить')
        delete = int(input())
        file = open('company.json', 'r', encoding='utf-8')
        if len(file.read()) != 0:
            file.seek(0)
            companies = json.load(file)
        else:
            print('нет организаций для поиска')
            break
        remove_company = None
        for company in companies:
            if company['inn'] == delete:
                remove_company = company
                break
        if remove_company is None:
            print('успешно удалено')
        else:
            companies.remove(remove_company)
        file = open('company.json', 'w+', encoding='utf-8')
        file.close()
        print(companies)


    #4
    elif answer == 4:
        print('закрытие программы')
        exit()