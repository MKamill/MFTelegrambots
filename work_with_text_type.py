import sqlite3 as lite

from first_telegram_bots import bot


@bot.message_handler(content_types=["text"])
def search_photo(message):
    try:
        name_of_photo = message.text
        conn = lite.connect(r'/storage/emulated/0/telegram/documents/photos.db')
        cursor = conn.cursor()
        sql = "SELECT path FROM img WHERE name=?"
        cursor.execute(sql, [name_of_photo])
        path = cursor.fetchone()  # or use fetchone()
        bot.send_message(message.chat.id, path)
        # bot.send_message(message.chat.id, fr'{path}'.replace('(','').replace(')','').replace('\'','').replace(',','') )

        doc = open(fr'{path}'.replace('(', '').replace(')', '').replace('\'', '').replace(',', ''), 'rb')
        # doc = open('//storage//emulated//0//telegram//documents//photos//Lamb_2020-08-09 03-19-26.929135.jpg', 'rb')
        bot.send_photo(message.chat.id, doc)
    except:
        bot.send_message(message.chat.id, 'пробую заново')
        try:
            search_photo(message)
        except:
            bot.send_message(message.chat.id, 'рекурсивная ошибка')


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
