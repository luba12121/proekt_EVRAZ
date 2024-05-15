import json
import telebot
from telebot import types

token2 = '6909925991:AAEi24htnDOZeUWEoZxQOXHTh_9RHEz8fk8'
bot = telebot.TeleBot(token2)

def get_employee(message):
    print(message.text)
    dannie_fio = []
    dannie_fio.append(message)
    bot.send_message(message.chat.id, text='Данные записаны', parse_mode='Markdown')
    textpol2 = 'Укажите телеграмм сотрудника'
    bot.send_message(message.chat.id, text=textpol2, parse_mode='Markdown')
    bot.register_next_step_handler(message, get_save)
def get_save(message):
    file = open('dannie_sotrudnika.json', 'w+', encoding='utf-8')
    #  dannie_sotrudnika= {
    #     "name": ,
    #     "tg":
    #
    # }
    # json.dump(dannie_sotrudnika, file, ensure_ascii=False)
    # file.close()


@bot.message_handler(content_types=['text'])
def get_message(message):
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

    if call.data == 'Посмотреть сотрудников':
        bot.send_message(call.from_user.id, text=call.message, parse_mode='Markdown')

    elif call.data == 'Добавить сотрудника':
        textpol = ('Укажите ФИО сотрудника')
        bot.send_message(call.from_user.id, text=textpol, parse_mode='Markdown')
        bot.register_next_step_handler(call.message, get_employee)


bot.polling(none_stop=True)


