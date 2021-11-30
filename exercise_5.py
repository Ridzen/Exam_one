# Бот показывает списки фильмов которые сейчас идут и выдает ссылку на сайт

import requests
import telebot
from bs4 import BeautifulSoup

TOKEN = '2113467680:AAERMhCBd08K_Oq72QA7vTodvFM6cvEwtJY'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

welcome_text = """
	Здраствуйте, приветствую моем телеграм боте! 
	Выберете кинотеатр!
"""

tsum_url = "https://tsumcinema.kg/?city=bishkek&facility=tsum-aichurek"
manas_url = 'http://manascinema.com/'
cosmopark_url = 'https://cinematica.kg/cinema/1'

error_msg = """
    Введите правильную команду!
"""

cinema_list = [
    {'name': 'Цум "Айчурек"'},
    {'name': 'Космопарк "IMAX30"'},
    {'name': 'Манас'},
]
cinema_ticket_category_data = []
cinema_ticket_category_name = []


@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text'])
def auto_handler(message):
    marcup = telebot.types.ReplyKeyboardMarkup()
    marcup.row(
        cinema_list[0].get('name'),
        cinema_list[1].get('name'),
        cinema_list[2].get('name'),
    )

    if message.text.lower() == 'start':
        bot.reply_to(
            message=message, text=welcome_text, reply_markup=marcup
        )

    if message.text == cinema_list[0]['name']:
        response = requests.get(tsum_url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_="sc-yf63q6-2 kLyqEz")
        category_list = div.find_all('a', class_='event-name')
        # div = soup.find('h2', class_="event-name").find_all('a')
        marcup = generate_tsum_ticket_category_btn(category_list)

        bot.send_message(
            chat_id=message.chat.id, text="Сейчас показывают:", reply_markup=marcup
        )
        bot.send_message(
            chat_id=message.chat.id, text=tsum_url, reply_markup=marcup
        )


    elif message.text == cinema_list[1]['name']:
        response = requests.get(cosmopark_url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_="hall-item")
        category_fail = div.find_all('a', class_='movie')
        marcap = generate_cosmopark_ticket_category_btn(category_fail)

        bot.send_message(
            chat_id=message.chat.id, text='Сейчас показывают', reply_markup=marcap
        )
        bot.send_message(
            chat_id=message.chat.id, text=cosmopark_url, reply_markup=marcap
        )

    elif message.text == cinema_list[2]['name']:
        response = requests.get(manas_url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_="m_info")
        category_titles = div.find_all('a', class_="m_title")
        marcap = generate_manas_ticket_category_btn(category_titles)

        bot.send_message(
            chat_id=message.chat.id, text='Сейчас показывают', reply_markup=marcap
        )
        bot.send_message(
            chat_id=message.chat.id, text=manas_url, reply_markup=marcap
        )


def generate_tsum_ticket_category_btn(category_list):
    category_names = [name.text for name in category_list]
    murcup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)

    for category_names in category_names:
        murcup.add(category_names)

    return murcup


def generate_cosmopark_ticket_category_btn(category_fail):
    category_names = [name.text for name in category_fail]
    murcup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)

    for category_names in category_names:
        murcup.add(category_names)

    return murcup


def generate_manas_ticket_category_btn(category_titles):
    category_names = [name.text for name in category_titles]
    murcup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)

    for category_names in category_names:
        murcup.add(category_names)

    return murcup


bot.polling()

