import datetime
import telebot
import time

f = open(r'/data/data/com.termux/files/home/telegram/bot_config.txt', 'r')
Token = f.read()
bot = telebot.TeleBot(Token)

disconnect_time = 0
status = False


@bot.message_handler(content_types=["text"])
def start_message(message):
    bot.send_message(message.chat.id, message.text)


"""модуль сохранения входящих изображений"""


@bot.message_handler(content_types=["photo"])
def incoming_photo(message):
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
    src = r'/data/data/com.termux/files/home/telegram/documents/photos/' + picture_name

    """открывает файл с назначенным путем в качестве нового файла
    и записывает в него полученное от пользователя изображение"""
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)
        new_file.close()


while True:
    try:
        bot.polling(none_stop=True)
    except:
        # local_time = 5
        time.sleep(0.01)
        # disconnect_time += local_time
        # print('----------------------[' + str(disconnect_time) + ']----------------------')
        continue
