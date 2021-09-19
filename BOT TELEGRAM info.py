import sys
import time
import telebot

TOKEN = "Сюда токен твоего бота"
bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=["text"])
# def welcome(message):
    #---------------------------------------
    #Ввывод имени пользователя
    #username = message.from_user.first_name
    #print(username,message.from_user.id)
    #---------------------------------------

    #---------------------------------------
    #Бот смотрит на сообщение пользователя и отвечает
    #if message.text.lower() == "Привет":
        #bot.send_message(message.chat.id, "Hello"
    #---------------------------------------



    #---------------------------------------
    #Бот пишет сообщение
    #bot.send_message(message.chat.id,"Hello")
    #---------------------------------------

    #---------------------------------------
    #Бот отправляет сообщения на указаный id
    #Мой id = 1624372687
    #bot.send_message('1624372687', f'User {username} send message: {message.text}')
    #---------------------------------------







# Запуск бота
bot.polling(none_stop=True)