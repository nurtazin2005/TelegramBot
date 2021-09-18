import sys
import time
import telebot

TOKEN = "1722906153:AAHFAtbaBSD_9xwK9ORZyB-wyE5RhdvRKY"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def welcome(message):
    username = message.from_user.first_name
    print(username,message.from_user.id)
    bot.send_message('1624372687', f'User {username} send message: {message.text}')

    bot.send_message(message.chat.id,"Hello")

    bot.send_message('1624372687', f'User {username} send message: {message.text}')







# Запуск бота
bot.polling(none_stop=True)