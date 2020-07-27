import telebot

bot = telebot.TeleBot( '1092838389:AAFc8XHNwhOyWVRKD2-nRTPUCFspbuzev0k')


@bot.message_handler(content_types=['text'])
def send_msg(message):
    if message.text == 'Карим':
        bot.send_message(message.chat.id, "лошара")
    elif message.text == 'Камиль':
        bot.send_message(message.chat.id, "крутой")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)