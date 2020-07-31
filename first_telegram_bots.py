import telebot

f = open(r'/storage/emulated/0/Android/data/ru.iiec.pydroid3.1/bot_config.txt', 'r')
Token = f.read()

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, введите ваш пароль:')

@bot.message_handler(content_types=['text'])
def send_msg(message):
    if message =='0909':
        bot.send_message(message.chat.id, 'Приветствуем Вас Юлия')
    elif message=='9090':
        bot.send_message(message.chat.id, 'Приветствуем Вас Камиль')



bot.polling(none_stop=True)
