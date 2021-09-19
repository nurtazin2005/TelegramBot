import time
import telebot
from telebot import types
#Фотография транспортаpip install pyTelegramBotAPI
# photo1 = open("photolink","rb")
# photo2 = open("photolink","rb")
#В words:0-Транспорт,1-Возмущение,2-Животные,3-Продукты,4-Фрукты,5-Овощи


#0-Транспорт  1-Возмущение 2-Животные 3-Продукты 4-Фрукты 5-Овощи 
words = ["🚦Транспорт - Ulaşım🚦\n\n🚁 Вертолет - Helikopter\n\n✈️ Самолет - Uçak\n\n🚉 Поезд - Tren\n\n⛴Корабль - gemi \n\n🚤 Лодка - Tekne\n\n🚲Велосипед - Bisiklet\n\n🚘 Автомобиль - Araba\n\n🚌 Автобус - Otobüs\n\n🚃 Трамвай - Tramvay\n\n🏍 Мотоцикл - Motor\n\n🛳 Паром - Vapur\n\n🚕 Такси - Taksi\n\n🚇 Метро - Metro\n\n🚑 Скорая - Ambulans",
"👺 Artık dayanamıyorum! - я не могу больше это терпеть!\n\n👺 Sabrım taşıyor! - мое терпение лопнуло!\n\n👺 Hele şükür! - ну наконец-то!\n\n👺 Bu beni delirtiyor! - это меня раздражает!\n\n👺 Rezalet! - это возмутительно!\n\n👺 Çok ayıp! - как не стыдно!\n\n👺 Of, bıktım artık! - как мне надоело!",
"🐶 Собака - Köpek\n\n🐈 Кошка - Kedi\n\n🐰 Кролик - Tavşan\n\n🐴 Лошадь - At\n\n🐦 Птица - Kuş\n\n🐯 Тигр - Kaplan\n\n🐻 Медведь - Ayı\n\n🐍 Змея - Yılan\n\n🐮 Корова - İnek\n\n🦁 Лев - Aslan",
"🧀 Сыр - Peynir\n\n🥛 Молоко - Süt\n\n🥚  Яйца - Yumurta \n\n🍞 Хлеб - Ekmek\n\n🍦 Йогурт - Yoğurt\n\n🧈 Масло - Yağ\n\n🥩 Мясо - Et\n\n🍨 Мороженое - Dondurma\n\n🧋  Какао - Kako\n\n☕️ Кофе - Kahve",
"🍎 Яблоко - Elma\n\n🍊 Апельсин - Portakal\n\n🥝 Киви - Kivi\n\n🍉 Арбуз- Karpuz\n\n🍌 Банан - Muz\n\n🍇 Виноград - Üzüm\n\n🍈 Дыня - Kavun\n\n🍐 Груша - Armut\n\n🍓 Клубника - Çilek\n\n🍑 Персик - Şeftali",
"\n\n🥔 Картошка - Patates\n\n🥕 Морковка - havuç\n\n🥑 Авокадо - Avokado\n\n🥒 Огурец - Salatalık\n\n🍆 Баклажан - Patlıcan\n\n🧅 Лук - Soğan\n\n🍅 Помидор - Domates\n\n🧄 Чеснок - Sarımsak\n\n🥦 Брокколи - Brokoli"]

bot = telebot.TeleBot('1722906153:AAHFAtbaBSD_9xwK9ORZyB-wyE5RhdzvRKY')

print('Bot launched')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.first_name
    bot.send_message('1624372687', f'User {username} send message: {message.text}')
    username = message.from_user.first_name
    print(username, message.from_user.id)
    bot.send_message(message.chat.id,f"Привет {message.from_user.first_name}")
    time.sleep(3)
    bot.send_message(message.chat.id, 'Я бот тестировщик')
    time.sleep(3)
    bot.send_message(message.chat.id, 'Я обладаю командами:\n\nКоманда "/words" запустит выбор слов\n\nКоманда "/group" выдаст сыллку в группу\n\nКоманда "/commands" выдаст список команд')


@bot.message_handler(commands=['help'])
def sendhelp(message):
    bot.reply_to(message,"Если нужна помощью,обращайся к Zer4")
# @TODO Add backend to this shit

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    username = message.from_user.first_name
    bot.send_message('1624372687', f'User {username} send message: {message.text}')
    username = message.from_user.first_name
    print(username, message.from_user.id)



    if message.text.lower() == "/words":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Ulaşım(Транспорт)', callback_data='first')
        keyboard.add(key_1)
        key_2 = types.InlineKeyboardButton(text='Tedirginlikler(Возмущения)', callback_data='second')
        keyboard.add(key_2)
        key_3 = types.InlineKeyboardButton(text='Hayvanlar(Животные)', callback_data='third')
        keyboard.add(key_3)
        key_4 = types.InlineKeyboardButton(text= 'Gıda(Продукты)',callback_data='fourth')
        keyboard.add(key_4)
        key_5 = types.InlineKeyboardButton(text= 'Yemiş(Фрукты)',callback_data='fifth')
        keyboard.add(key_5)
        key_6 = types.InlineKeyboardButton(text= 'Sebze(Овощи)',callback_data='sixth')
        keyboard.add(key_6)


        bot.send_message(message.from_user.id, text='Выбери список', reply_markup=keyboard)
    
    elif message.text.lower() == "/commands":
        bot.send_message(message.chat.id,'Команда "/words" запустит выбор слов\n\nКоманда "/group" выдаст сыллку в группу')

    elif message.text.lower() == "/group":
        bot.send_message(message.chat.id,"Сыллка на группу:\nhttps://t.me/joinchat/KXW0dltmSdFjYTdi")

    else:
        bot.reply_to(message,"Я не понимаю команды,для выввода команд введите:/commands")

    bot.send_message('1695139772', f'User {username} send message: {message.text}')



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # print(call)
    if call.data == "first":
        # Отправляем текст в Телеграм
        # bot.send_photo(call.message.chat.id,photo1)
        bot.send_message(call.message.chat.id,words[0])
        
    elif call.data == "second":
        # Отправляем текст в Телеграм
        # bot.send_photo(call.message.chat.id, photo2)
        bot.send_message(call.message.chat.id,words[1])

    elif call.data == "third":
        bot.send_message(call.message.chat.id,words[2])
    
    elif call.data == "fourth":
        bot.send_message(call.message.chat.id,words[3])

    elif call.data == "fifth":
        bot.send_message(call.message.chat.id,words[4])
    
    elif call.data == "sixth":
        bot.send_message(call.message.chat.id,words[5])



bot.polling(none_stop=True)