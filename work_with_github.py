import requests
import request_py as req


def get_text(incoming_url):
    rs = requests.get(incoming_url)
    return rs.content


url = 'https://raw.githubusercontent.com/MKamill/MFTelegrambots/master/first_telegram_bots.py'
print(get_text(
    url))
f = open('request_py.py', 'w')
f.write(str((get_text(url)).decode('utf-8')))

req
