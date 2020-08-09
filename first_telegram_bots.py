import subprocess
import work_with_keyboard_and_buttons as keyboard
import work_with_connection as connection
import work_with_text_type as text


text.start_message()
keyboard.start_message()
keyboard.query_handler()

while True:
    try:
        connection.bot.polling(none_stop=True)
    except:
        subprocess.call(['./reboot.sh'])
