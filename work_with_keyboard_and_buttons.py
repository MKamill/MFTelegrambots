import telebot
import work_with_connection as connection
import work_with_text_type as text
import work_with_bot_photos as photo


@connection.bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Добавить', callback_data='add'))
    markup.add(telebot.types.InlineKeyboardButton(text='Найти', callback_data='search'))
    connection.bot.send_message(message.chat.id, text="Выберите действие 👇", reply_markup=markup)
#2

@connection.bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    connection.bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == 'add':
        photo.main_inc_photo(call.message.chat.id)
    elif call.data == 'search':
        text.main_search(call.message.chat.id)
