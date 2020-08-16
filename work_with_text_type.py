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


""""функция активации возможности серфить по материалу"""


def main_search(ch_id):
    # у пользователя запрашивается тег по которому будем искать информацию
    connection.bot.send_message(ch_id, 'Введите название искомого материала 🔎')

    # обработчик введенного сообщения
    # возвращает картинку в диалог в случае нахождения
    @connection.bot.message_handler(content_types=['text'])
    def search_photo(message):
        try:
            # подключаемся к базе данных
            conn = lite.connect(r'/storage/emulated/0/telegram/documents/photos.db')
            cursor = conn.cursor()

            # статус проверки наличия введенного пользователем тега
            status_of_process = False
            # выбираются все записи
            cursor.execute("SELECT * FROM img")
            all_names = cursor.fetchall()

            # проходим по записям в поисках совпадающего тега
            # иначе оповещаем пользователя о том, что совпадений не найдено
            for name in all_names:
                # индексирование на [0]==обращение к 1 полю (name) кортежа all_names
                if name[0] == message.text:
                    # в случае совпадения статус меняем на правду
                    status_of_process = True
            # если статус правда присваиваем переменной имя введенного
            # тега для дальнейшего поиска
            if status_of_process:
                name_of_photo = message.text
            else:
                connection.bot.send_message(message.chat.id, 'отсутствует информация по данному тегу')
                return
            # если статус правда ищем в базе путь соответствующий тегу
            # и отсылаем в диалог фото по найденному пути
            if status_of_process:
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
