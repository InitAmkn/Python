# python -m pip install pyTelegramBotAPI

import telebot.types
from telebot import TeleBot


bot = TeleBot('5415154699:AAGcZYgW1xfwKtVybAL-pLBBIusLophuzwU')


def summator(text):
    lst = text.split()
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
        return str(int(lst[0]) + int(lst[1]))
    return 'Это некорректный запрос'


def censorship(delete_word, something_text):
    something_text = something_text + "|"
    while (something_text.find(delete_word) != -1):
        x = something_text.find(delete_word)
        i_start = x
        i_finish = x
        while something_text[i_start].isalpha() == True and i_start > 0:
            i_start -= 1
        while something_text[i_finish].isalpha() == True and i_finish < len(something_text):
            i_finish += 1
        something_text = something_text.replace(
            something_text[i_start:i_finish], '', 1)
        x = something_text.find(delete_word)
    return something_text[:-1]


'''
@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text))
'''

@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=censorship("абв",msg.text))

bot.polling()


# При помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#python -m venv qqq
