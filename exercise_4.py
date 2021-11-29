# Создать телеграм-бота,
# который считывает входящие сообщения и выдает сколько раз повторяются в этом сообщении гласные буквы.
# Для простоты считайте, что все сообщения будут присылаться на латинице.
# Не забывайте,
# что гласные буквы могут быть в верхнем регистре

import telebot

TOKEN = "2140846951:AAEuTTCxhfx55xvyut5K5Z2j8WypXnD0tCI"

welcome_text = """
    Пиши что хочешь, будут только гласные
"""
bot = telebot.TeleBot(TOKEN)

letters = ['а, о, у, ы, э, е, и, ю, я']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Салам')


@bot.message_handler(content_types=['text'])
def text_message(message):

    count = 0
    for i in message.text:
        if i in letters:
            count +=1

    bot.send_message(message.chat.id, count)


bot.polling(none_stop=True)
