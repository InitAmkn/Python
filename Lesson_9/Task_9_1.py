# python -m pip install pyTelegramBotAPI

import telebot.types
from telebot import TeleBot


bot = TeleBot('')


def summator(text):
    lst = text.split()
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
        return str(int(lst[0]) + int(lst[1]))
    return 'Это некорректный запрос'


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text))


bot.polling()


# При помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#python -m venv qqq
