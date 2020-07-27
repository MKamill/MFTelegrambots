import telebot
import work_with_email as email
import defsForAnalysis as analysis

bot = telebot.TeleBot('1092838389:AAFc8XHNwhOyWVRKD2-nRTPUCFspbuzev0k')


@bot.message_handler(content_types=['text'])
def send_msg(message):
    if analysis.call_all_defs(message.text):
        email.the_process_of_sending('2:45')

    if message.text == 'Карим':
        bot.send_message(message.chat.id, "лошара")
    elif message.text == 'Камиль':
        bot.send_message(message.chat.id, "крутой")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
