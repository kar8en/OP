import telebot
from telebot import types
bot = telebot.TeleBot('6028886665:AAGds6brnWC6F03-sC_4XMlhPZqHm5sHPGY')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Календарь приёма')
    item2 = types.KeyboardButton('Алгоритм поступления')
    item3 = types.KeyboardButton('Олимпиады')
    item4 = types.KeyboardButton('Ход приёма')
    markup.add(item1, item2, item3, item4)
    photo_red_1 = open('red_1.png', 'rb')
    bot.send_photo(message.chat.id, photo_red_1)
    bot.send_message(message.chat.id, '<b>Выберите интересующую информацию.</b>',reply_markup=markup, parse_mode='html')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Календарь приёма':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Очная', 'Заочная')
        markup.row('Назад')
        bot.send_message(message.chat.id, 'Выберите форму обучения:', reply_markup=markup)
    elif message.text == 'Алгоритм поступления':
        photo_red_2 = open('red_2.png', 'rb')
        bot.send_photo(message.chat.id, photo_red_2)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://priem.guap.ru/mag"))
        bot.send_message(message.chat.id, "Вы также можете посмотреть алгоритм поступления на сайте приёмной комиссии ГУАП", reply_markup=markup)
    elif message.text == 'Олимпиады':
        photo_red_3 = open('red_3.png', 'rb')
        bot.send_photo(message.chat.id, photo_red_3)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://priem.guap.ru/mag/magister_olymp"))
        bot.send_message(message.chat.id, "Вы также можете посмотреть информацию по олимпиадам на сайте приёмной комиссии ГУАП", reply_markup=markup)
    elif message.text == 'Ход приёма':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://priem.guap.ru/mag/start_lists"))
        bot.send_message(message.chat.id,"Вы можете следить за ходом приёма на сайте приёмной комиссии ГУАП", reply_markup=markup)
    elif message.text == 'Очная':
        photo_red_4 = open('red_4.png', 'rb')
        bot.send_photo(message.chat.id, photo_red_4)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить сайт", url ="https://priem.guap.ru/mag/calendar"))
        bot.send_message(message.chat.id, "Вы также можете посмотреть календарь приёма на официальном сайте", reply_markup= markup)
    elif message.text == 'Заочная':
        photo_red_5 = open('red_5.png', 'rb')
        bot.send_photo(message.chat.id, photo_red_5)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://priem.guap.ru/mag/calendar"))
        bot.send_message(message.chat.id, " Вы также можете посмотреть календарь приёма на официальном сайте",reply_markup=markup)
    elif message.text == 'Назад':
        start(message)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, выберите одну из кнопок')
bot.polling()
