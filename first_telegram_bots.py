import datetime
import telebot
from PIL import Image, ImageDraw
import subprocess
import sqlite3 as lite

f = open(r'/data/data/com.termux/files/home/telegram/bot_config.txt', 'r')
Token = f.read()
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Добавить', callback_data='add'))
    markup.add(telebot.types.InlineKeyboardButton(text='Найти', callback_data='search'))
    bot.send_message(message.chat.id, text="Выберите действие 👇", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def search_photo(message):
    try:
        name_of_photo = message.text
        conn = lite.connect(r'/storage/emulated/0/telegram/documents/photos.db')
        cursor = conn.cursor()
        sql = "SELECT path FROM img WHERE name=?"
        cursor.execute(sql, [name_of_photo])
        path = cursor.fetchone()  # or use fetchone()
        out_img = Image.open(path)
        bot.send_photo(message.chat.id, out_img)
    except:
        bot.send_message(message.chat.id, 'пробую заново')
        try:
            search_photo(message)
        except:
            bot.send_message(message.chat.id, 'рекурсивная ошибка')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == 'add':
        answer = 'Отправьте фото с подписью 📝'
    elif call.data == 'search':
        answer = 'Введите название искомого материала 🔎'
    bot.send_message(call.message.chat.id, answer)


@bot.message_handler(content_types=["text"])
def start_message(message):
    try:
        bot.send_message(message.chat.id, message.text)
    except:
        bot.send_message(message.chat.id, 'пробую заново')
        try:
            start_message(message)
        except:
            bot.send_message(message.chat.id, 'рекурсивная ошибка')


"""модуль сохранения входящих изображений"""


@bot.message_handler(content_types=["photo"])
def incoming_photo(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        caption = f'{message.from_user.last_name} | {message.from_user.first_name} | {message.from_user.username}'
        bot.send_photo(1361637547, downloaded_file, caption)

        """задается имя картинки согласно комментарию к фото + время отправки 
        с разршением .jpg в случае наличия комментария,
        иначе изображению присваивается статус потерявшейся + время отправки"""
        if message.caption is not None:
            picture_name = str(message.caption) + '_' + str(datetime.datetime.now()).replace(':', '-') + '.jpg'
        else:
            picture_name = 'lost image_' + str(datetime.datetime.now()).replace(':', '-') + '.jpg'

        """путь для развертывания на телефоне 4x"""
        src = r'/storage/emulated/0/telegram/documents/photos/' + picture_name

        """открывает файл с назначенным путем в качестве нового файла
        и записывает в него полученное от пользователя изображение"""
        with open(src, "wb") as new_file:
            new_file.write(downloaded_file)
            new_file.close()

        con = lite.connect(r'/storage/emulated/0/telegram/documents/photos.db')
        cur = con.cursor()
        cur.execute("INSERT INTO img VALUES (?,?)", (message.caption, src,))
        con.commit()

    except:
        bot.send_message(message.chat.id, 'пробую заново')
        try:
            incoming_photo(message)
            bot.send_message(message.chat.id, 'фото добавлено')
        except:
            bot.send_message(message.chat.id, 'рекурсивная ошибка')


while True:
    try:
        bot.polling(none_stop=True)
    except:
        subprocess.call(['./reboot.sh'])
