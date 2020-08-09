import telebot
from first_telegram_bots import bot


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Добавить', callback_data='add'))
    markup.add(telebot.types.InlineKeyboardButton(text='Найти', callback_data='search'))
    bot.send_message(message.chat.id, text="Выберите действие 👇", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == 'add':
        answer = 'Отправьте фото с подписью 📝'
    elif call.data == 'search':
        answer = 'Введите название искомого материала 🔎'
    bot.send_message(call.message.chat.id, answer)