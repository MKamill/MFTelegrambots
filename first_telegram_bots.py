import telebot


f = open(r'/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/bot_config.txt', 'r')
Token = f.read()

bot = telebot.TeleBot('1092838389:AAFc8XHNwhOyWVRKD2-nRTPUCFspbuzev0k')

# 11 дай уйти

@bot.message_handler(content_types=['text'])
def send_msg(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
