import json
import telebot
from telebot import types

token2 = '6909925991:AAEi24htnDOZeUWEoZxQOXHTh_9RHEz8fk8'
bot = telebot.TeleBot(token2)

dannie_fio = []
dannie_tg = []

def get_employee(message):
    # print('get_employee')
    global dannie_fio
    dannie_fio.append(message.text)
    bot.send_message(message.chat.id, text='*Данные записаны*', parse_mode='Markdown')
    textpol2 = 'Укажите телеграмм сотрудника'
    bot.send_message(message.chat.id, text=textpol2, parse_mode='Markdown')
    bot.register_next_step_handler(message, get_save)


def get_save(message):
    # print('get_save')
    global dannie_fio
    # global message
    dannie_tg.append(message.text)
    bot.send_message(message.chat.id, text='*Данные записаны*', parse_mode='Markdown')


    file = open('dannie_sotrudnika.json', 'w+', encoding='utf-8')
    dannie_sotrudnika= {
        "name": dannie_fio,
        "tg": dannie_tg
        }
    json.dump(dannie_sotrudnika, file, ensure_ascii=False)
    file.close()


    keyboard = types.InlineKeyboardMarkup()
    button10 = types.InlineKeyboardButton(text='Да', callback_data='Да')
    keyboard.add(button10)
    button20 = types.InlineKeyboardButton(text='Нет', callback_data='Нет')
    keyboard.add(button20)
    bot.send_message(message.from_user.id, text = 'Хотите добавить еще одного сотрудника?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_message(message):
    print('message')
    print(message)
    if message.text == '/start':
        bot.set_my_commands(
            commands=[
                types.BotCommand('/command1', 'начать работу с ботом')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )

        bot.send_message(message.from_user.id,
                         text='Здравствуйте!Представляем главных должностных лиц цехов')

        keyboard = types.InlineKeyboardMarkup()
        button10 = types.InlineKeyboardButton(text='Посмотреть сотрудников ', callback_data='Посмотреть сотрудников')
        keyboard.add(button10)
        button20 = types.InlineKeyboardButton(text='Добавить сотрудника', callback_data='Добавить сотрудника')
        keyboard.add(button20)
        print(keyboard)
        bot.send_message(message.from_user.id,text='Главные в цехе',reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    print(call)
    if call.data == 'Посмотреть сотрудников':
        file1 = open('dannie_sotrudnika.json', 'r+', encoding='utf-8')
        workers = json.load(file1)
        print(workers)
        text = '*Список сотрудников:*\n\n'
        for i in range(len(workers['name'])):
            text += '_Имя сотрудника:_ ' + workers['name'][i] + '\n'
            text += '_Телеграм сотрудника:_ ' + workers['tg'][i] + '\n\n'
        bot.send_message(call.from_user.id, text = text, parse_mode='Markdown')
        # bot.send_message(call.from_user.id, text= workers['tg'], parse_mode='Markdown')
    elif call.data == 'Добавить сотрудника':
            textpol = ('Укажите ФИО сотрудника')
            bot.send_message(call.from_user.id, text=textpol, parse_mode='Markdown')
            bot.register_next_step_handler(call.message, get_employee)
    elif call.data == 'Да':
        bot.send_message(call.from_user.id, text='Укажите ФИО сотрудника', parse_mode='Markdown')
        bot.register_next_step_handler(call.message, get_employee)
    elif call.data == 'Нет':
            bot.send_message(call.from_user.id, text='_Указанные ранеее сотрудники успешно добавлены!_',parse_mode='Markdown')



bot.polling(none_stop=True)


