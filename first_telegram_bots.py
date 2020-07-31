import types

import telebot
import time

f = open(r'/storage/emulated/0/Android/data/ru.iiec.pydroid3.1/bot_config.txt', 'r')
Token = f.read()

bot = telebot.TeleBot(Token)

disconnect_counter = 0
status = False


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, введите ваш пароль:')


@bot.message_handler(content_types=['text'])
def send_msg(message):
    if message.text == '0909':
        bot.send_message(message.chat.id, 'Приветствуем Вас Юлия')
        keyboard = types.InlineKeyboardMarkup()

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')

        keyboard.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')

        keyboard.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == '9090':
        bot.send_message(message.chat.id, 'Приветствуем Вас Камиль')
    else:
        bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):
    if call.data == "zodiac":
        msg='вы нажали на кнопку'
        bot.send_message(call.message.chat.id, msg)

while True:
    try:
        bot.polling(none_stop=True)
    except:
        local_time = float(1)
        local_time = local_time * 10
        time.sleep(local_time)
        disconnect_counter += 1
        print('----------------------[' + str(disconnect_counter/60) + ']----------------------')
        continue
