import telebot

f = open(r'/data/data/com.termux/files/home/telegram/bot_config.txt', 'r')
Token = f.read()
bot = telebot.TeleBot(Token)
