import datetime
import urllib

import telebot
import time

# f = open(r'/storage/emulated/0/Android/data/ru.iiec.pydroid3.1/bot_config.txt', 'r')
# Token = f.read()
Token = '1092838389:AAFc8XHNwhOyWVRKD2-nRTPUCFspbuzev0k'

bot = telebot.TeleBot('1092838389:AAFc8XHNwhOyWVRKD2-nRTPUCFspbuzev0k')

disconnect_counter = 0
status = False


@bot.message_handler(content_types=["text"])
def start_message(message):
    if message.text == 'войти' or message.text == 'Войти':
        bot.send_message(message.chat.id, 'Здравствуйте, введите ваш пароль:')


"""модуль сохранения входящих изображений"""


@bot.message_handler(content_types=["photo"])
def incoming_photo(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    """задается имя картинки согласно комментарию к фото + время отправки 
    с разршением .jpg в случае наличия комментария,
    иначе изображению присваивается статус потерявшейся + время отправки"""
    if message.caption is not None:
        picture_name = str(message.caption) + '_' + str(datetime.datetime.now()).replace(':', '-') + '.jpg'
    else:
        picture_name = 'lost image_' + str(datetime.datetime.now()).replace(':', '-') + '.jpg'

    """назначается путь для хранения входящего изображения"""
    src = r'C:/Users/79876/PycharmProjects/Telebots/documents/photos/' + picture_name

    """путь для развертывания на телефоне"""
    # src = r'/storage/emulated/0/Android/data/ru.iiec.pydroid3.1/documents/photos/'+ picture_name


    """открывает файл с назначенным путем в качестве нового файла
    и записывает в него полученное от пользователя изображение"""
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)


while True:
    try:
        bot.polling(none_stop=True)
    except:
        local_time = 10
        time.sleep(local_time)
        disconnect_counter += 1
        print('----------------------[' + str(disconnect_counter / 60) + ']----------------------')
        continue
