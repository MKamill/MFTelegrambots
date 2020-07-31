import telebot

f = open('bot_config', 'r')
Token = f.read()

bot = telebot.TeleBot(token=Token)

# Good Kamill, you did it

@bot.message_handler(content_types=['text'])
def send_msg(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
