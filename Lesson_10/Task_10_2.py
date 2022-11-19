import telebot
from time import time

bot = telebot.TeleBot('')
with open('logfile.log', 'a') as f_log:
    print(time(), 'Бот запущен', file=f_log)


def do_log(msg: telebot.types.Message):
    with open('logfile.log', 'a') as f_log:
        print(
            time(), f'Пользователь ({msg.from_user.id}) прислал сообщение: {msg.text}', file=f_log)


@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    do_log(msg)
    bot.send_message(msg.from_user.id,
                     'Вас приветствует самый лучший калькулятор.')


@bot.message_handler()
def answer(msg: telebot.types.Message):
    do_log(msg)
    bot.send_message(msg.from_user.id, 'Введите первое число.')
    bot.register_next_step_handler(msg, second, last=int(msg.text))


def second(msg: telebot.types.Message, last):
    do_log(msg)
    bot.send_message(msg.from_user.id, f'Текущее значение {last}')
    bot.send_message(msg.from_user.id, 'Введите ещё одно число.')
    bot.register_next_step_handler(msg, second, last=last + int(msg.text))


bot.polling()
