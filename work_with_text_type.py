import sqlite3 as lite
import work_with_connection as connection


# @connection.bot.message_handler(content_types=["text"])
# def start_message(message):
#     try:
#         connection.bot.send_message(message.chat.id, message.text)
#     except:
#         connection.bot.send_message(message.chat.id, 'пробую заново')
#         try:
#             start_message(message)
#         except:
#             connection.bot.send_message(message.chat.id, 'рекурсивная ошибка')


def main_search(ch_id):
    connection.bot.send_message(ch_id, 'Введите название искомого материала 🔎')

    @connection.bot.message_handler(content_types=['text'])
    def search_photo(message):
        try:
            conn = lite.connect(r'/storage/emulated/0/telegram/documents/photos.db')
            cursor = conn.cursor()
            status_of_proc = False

            cursor.execute("SELECT name FROM img")
            all_names = cursor.fetchall()
            connection.bot.send_message(message.chat.id, all_names)

            for name in all_names:
                if name == message.text:
                    status_of_proc = True
            if status_of_proc:
                name_of_photo = message.text
            else:
                connection.bot.send_message(message.chat.id, 'отсутствует информация по данному тегу')

            """проверить существует ли искомая инфа в базе иначе переспросить
            ошибка вызывает аборт"""

            sql = "SELECT path FROM img WHERE name=?"
            cursor.execute(sql, [name_of_photo])
            path = cursor.fetchone()
            doc = open(fr'{path}'.replace('(', '').replace(')', '').replace('\'', '').replace(',', ''), 'rb')
            connection.bot.send_photo(message.chat.id, doc)
            return
        except:
            try:
                search_photo(message)
                return
            except:
                connection.bot.send_message(message.chat.id, 'рекурсивная ошибка')
                return
