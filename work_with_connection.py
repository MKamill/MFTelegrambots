import telebot
import subprocess
import work_with_connection as connection

f = open(r'/data/data/com.termux/files/home/telegram/bot_config.txt', 'r')
Token = f.read()
bot = telebot.TeleBot(Token)


@connection.bot.message_handler(commands=['reboot'])
def start_message(message):
    subprocess.call(['./reboot.sh'])
