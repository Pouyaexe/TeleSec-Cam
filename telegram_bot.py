# telegram_bot.py
import telebot
from telebot import types
import config  # Import the config.py file

# Use the values from config.py
BOT_TOKEN = config.BOT_TOKEN
TELEGRAM_USER_ID = config.TELEGRAM_USER_ID

# Initialize the Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)

def send_capture_button():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    capture_btn = types.KeyboardButton('Capture')
    markup.add(capture_btn)
    bot.send_message(TELEGRAM_USER_ID, "Press the button to capture a photo:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == 'capture' and message.chat.id == TELEGRAM_USER_ID)
def handle_capture_message(message):
    with open('capture_command.txt', 'w') as file:  # Create a file as a flag
        pass  # The existence of the file indicates the 'capture' command was received
    print('Capture command received.')  # Print a message to the terminal


def send_message_to_telegram(message):
    bot.send_message(TELEGRAM_USER_ID, message)

def send_photo_to_telegram(file_path):
    with open(file_path, 'rb') as photo:
        bot.send_photo(TELEGRAM_USER_ID, photo)

if __name__ == "__main__":
    send_capture_button()  # Send the message with the Capture button when the script is run
    bot.polling(none_stop=True)