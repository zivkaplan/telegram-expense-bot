from dotenv import load_dotenv
from os import getenv
import telebot

load_dotenv()
API_KEY = getenv('API_KEY')

hideBoard = telebot.types.ReplyKeyboardRemove()

bot = telebot.TeleBot(API_KEY)


@bot.message_handler()
def SendPhoto(message):
        bot.send_photo(message.chat.id, open("src/ziv.jpg","rb"))

bot.polling()
