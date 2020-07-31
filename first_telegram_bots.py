import telebot

f = open(r'/storage/emulated/0/Android/data/ru.iiec.pydroid3.1/bot_config.txt', 'r')
Token = f.read()

bot = telebot.TeleBot(Token)

# 11 дай уйти

@bot.message_handler(content_types=['text'])
def send_msg(message):
    bot.send_message(message.chat.id, 'Камиль ты гений')

bot.polling(none_stop=True)
