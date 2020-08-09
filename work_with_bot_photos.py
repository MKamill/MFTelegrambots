import work_with_connection as connection

import datetime
import sqlite3 as lite

"""модуль сохранения входящих изображений"""


@connection.bot.message_handler(content_types=["photo"])
def incoming_photo(message):
    try:
        file_info = connection.bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = connection.bot.download_file(file_info.file_path)
        caption = f'{message.from_user.last_name} | {message.from_user.first_name} | {message.from_user.username}'
        connection.bot.send_photo(1361637547, downloaded_file, caption)

        """задается имя картинки согласно комментарию к фото + время отправки 
        с разршением .jpg в случае наличия комментария,
        иначе изображению присваивается статус потерявшейся + время отправки"""
        if message.caption is not None:
            picture_name = str(message.caption) + '_' + str(datetime.datetime.now()).replace(':', '-') + '.jpg'
        else:
            picture_name = 'lost image_' + str(datetime.datetime.now()).replace(':', '-') + '.jpg'

        """путь для развертывания на телефоне 4x"""
        src = r'/storage/emulated/0/telegram/documents/photos/' + picture_name
        dumb_src = '//storage//emulated//0//telegram//documents//photos//' + picture_name

        """открывает файл с назначенным путем в качестве нового файла
        и записывает в него полученное от пользователя изображение"""
        with open(src, "wb") as new_file:
            new_file.write(downloaded_file)
            new_file.close()

        con = lite.connect(r'/storage/emulated/0/telegram/documents/photos.db')
        cur = con.cursor()
        cur.execute("INSERT INTO img VALUES (?,?)", (message.caption, dumb_src,))
        con.commit()

    except:
        connection.bot.send_message(message.chat.id, 'пробую заново')
        try:
            incoming_photo(message)
            connection.bot.send_message(message.chat.id, 'фото добавлено')
        except:
            connection.bot.send_message(message.chat.id, 'рекурсивная ошибка')
