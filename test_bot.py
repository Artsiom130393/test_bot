# Продолжить разработку телеграмм бота. Добавить опции:
# -'Хочу гулять'
# -'Хочу спать'
# -'Хочу шутку'

import telebot
from telebot import types
# 5688715269:AAGES3tzeaLkpl1xYn1JTvA-xvwKdYppQOQ

token = '5688715269:AAGES3tzeaLkpl1xYn1JTvA-xvwKdYppQOQ'
bot = telebot.TeleBot(token)

def create_keyboard(): #функция для создания кнопок
    keyboard = types.InlineKeyboardMarkup() #создаем пустую клавиатуру (виртуальную)
    drink_btn = types.InlineKeyboardButton(text='Хочу пить!', callback_data='1') #создаем конкретную кнопку на клавиатуру
    eat_btn = types.InlineKeyboardButton(text='Хочу есть!', callback_data='2')
    gul_btn = types.InlineKeyboardButton(text='Хочу гулять!', callback_data='3')
    son_btn = types.InlineKeyboardButton(text='Хочу спать!', callback_data='4')
    shutka_btn = types.InlineKeyboardButton(text='Хочу шутку!', callback_data='5')
    keyboard.add(drink_btn) #добавили кнопку на клавиатуру
    keyboard.add(eat_btn)
    keyboard.add(gul_btn)
    keyboard.add(son_btn)
    keyboard.add(shutka_btn)
    return keyboard

@bot.message_handler(commands=['start']) #декоратор при перехвате команды start запустит функцию start_bot
def start_bot(message):
    keyword = create_keyboard()
    bot.send_message(
        message.chat.id,
        'Добрый день! Сделайте выбор!',
        reply_markup=keyword
    )

@bot.callback_query_handler(func=lambda call:True) #queary_handler перехватывает запросы
def callback(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == '1':
            img = open('7fa536ce4777b71075b6f223b784b3b2.jpeg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo= img,
                caption='Картинка воды',
                reply_markup=keyboard
            )
        if call.data == '2':
            img = open('picca-pizza-eda.jpeg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка еды',
                reply_markup=keyboard
            )
        if call.data == '3':
            img = open('1647929027_2-kartinkin-net-p-progulka-kartinki-2.jpeg',
                       'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка прогулки',
                reply_markup=keyboard
            )
        if call.data == '4':
            img = open('1646023032_1-kartinkin-net-p-kartinki-dlya-sna-1.jpeg',
                       'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка сна',
                reply_markup=keyboard
            )
        if call.data == '5':
            img = open('17417.jpeg',
                       'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка шутки',
                reply_markup=keyboard
            )
if __name__ == '__main__':
    bot.polling(none_stop=True) #включаем работу бота без остановок


