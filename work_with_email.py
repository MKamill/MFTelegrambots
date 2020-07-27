# импорт библиотеки для работы с почтой
import smtplib
# импорт библиотеки для работы со звуковым сигналом
import winsound

# настройка частоты  сигнала
freq = 650
# настройка продолжительности сигнала
dur = 100

# исходные данные
_from = 'mirgayazow2014@yandex.ru'
password = '6601052_0909011kK'
to = 'mirgayazovk@gmail.com'
message = 'good night Kamill :)'
subject = 'Test email from Python'
domain_and_port = 'smtp.yandex.ru: 465'


def the_process_of_sending(mess):
    # инициализация подключения
    server = smtplib.SMTP_SSL(domain_and_port)
    # авторизация
    server.login(_from, password)
    # определение содержмого
    body = "\r\n".join((
        "From: %s" % _from,
        "To: %s" % to,
        "Subject: %s" % subject,
        "",
        str(mess)
    ))
    # от кого, кому, что
    server.sendmail(_from, to, body)
    # отключаем соединение
    server.quit()
    # сигнализируем о завершении работы скрипта
    winsound.Beep(freq, dur)


