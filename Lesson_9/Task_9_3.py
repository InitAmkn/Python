# python -m pip install pyTelegramBotAPI

from asyncio import Task
import telebot.types
from telebot import TeleBot


bot = TeleBot('')




'''
@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text))
'''


from random import randint

def game_of_candy(total_quantity_of_candies, max_сan_get_candy=28, bot=False):

    if bot:
        player = randint(2, 3)
        if player == 2:
            player = 1
    if bot == False:
        player = randint(1, 2)

    now_candy = total_quantity_of_candies
    while now_candy > max_сan_get_candy:
        correct_input = False
        if player == 1 or player == 2:
            while correct_input == False:
                print(f">>>Количество конфет на столе: {now_candy}")
                try:
                    take_candy = int(
                        input(f"Игрок #{player} введите желаемое кол-во конфет: "))
                    if take_candy > max_сan_get_candy:
                        print(
                            f"---Пожадничал, максимум можно взять {max_сan_get_candy} конфет")
                    elif take_candy <= 0:
                        print(
                            f"---Нельзя брать меньше 1 конфеты")
                    else:
                        correct_input = True
                except:
                    print("---Некорректный ввод, прошу ввести цифры")

        if player == 3:
            take_candy = artificial_intelligence(now_candy, max_сan_get_candy)
            print(f">>>Количество конфет на столе: {now_candy}")
            print(f"Бот взял конфет: {take_candy}")

        now_candy -= take_candy
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        if bot == True and player == 2:
            player = 3
        elif player == 3:
            player = 1

    else:
        if bot == True and player == 3:
            print(f"Бот забирает оставшиеся {now_candy}")
            print(f"Человеки будут порабощены")
        if player == 1 or player == 2:
            print(f"Игрок #{player} забирает оставшиеся {now_candy}")
            print(f"Игрок #{player} победил")





def player_intelligence(text,now_candy,max_сan_get_candy):
    take = int(text)
    now_candy -= take
    return now_candy


def artificial_intelligence(now_candy, max_сan_get_candy):
    temp = now_candy - \
        now_candy // (max_сan_get_candy + 1)*(max_сan_get_candy + 1)
    if temp > 0:
        return temp
    else:
        return randint(1, max_сan_get_candy)




now_candy = 228
max_сan_get_candy = 28
@bot.message_handler()
def echo(msg: telebot.types.Message):
    
    bot.send_message(chat_id=msg.from_user.id, text= player_intelligence(msg.text,now_candy,max_сan_get_candy))
    bot.send_message(chat_id=msg.from_user.id, text= f"Бот взял :{artificial_intelligence(now_candy,max_сan_get_candy)}")
bot.polling()


# При помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#python -m venv qqq
