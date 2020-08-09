import sqlite3 as lite
import work_with_connection as connection


@connection.bot.message_handler(content_types=["text"])
def search_photo(message):
    try:
        name_of_photo = message.text
        conn = lite.connect(r'/storage/emulated/0/telegram/documents/photos.db')
        cursor = conn.cursor()
        sql = "SELECT path FROM img WHERE name=?"
        cursor.execute(sql, [name_of_photo])
        path = cursor.fetchone()  # or use fetchone()
        connection.bot.send_message(message.chat.id, path)
        doc = open(fr'{path}'.replace('(', '').replace(')', '').replace('\'', '').replace(',', ''), 'rb')
        connection.bot.send_photo(message.chat.id, doc)
    except:
        connection.bot.send_message(message.chat.id, 'пробую заново')
        try:
            search_photo(message)
        except:
            connection.bot.send_message(message.chat.id, 'рекурсивная ошибка')


@connection.bot.message_handler(content_types=["text"])
def start_message(message):
    try:
        connection.bot.send_message(message.chat.id, message.text)
    except:
        connection.bot.send_message(message.chat.id, 'пробую заново')
        try:
            start_message(message)
        except:
            connection.bot.send_message(message.chat.id, 'рекурсивная ошибка')
