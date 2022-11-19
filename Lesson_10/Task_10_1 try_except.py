import telebot
flag = True
while flag:
    try:
        a = input()
        if not (a.isdigit() and a.startswith('8') and len(a) == 11):
            raise TypeError('Номер телефона некорректный')
    except ValueError as e:
        print('Ошибка.', e)
    except TypeError as e:
        print(f'Ошибка. {e}')
    else:
        flag = False
    finally:
        print('Конец блока try')


bot = telebot.TeleBot('')


dct = {}


@bot.message_handler()
def answer(msg: telebot.types.Message):
    if msg.from_user.id not in dct:
        dct[msg.from_user.id] = [1]

    if dct[msg.from_user.id][0] == 1:
        bot.send_message(msg.from_user.id, 'Введите первое число.')
        bot.send_message(msg.from_user.id, f'{dct}')
        dct[msg.from_user.id][0] = 2

    elif dct[msg.from_user.id][0] == 2:
        dct[msg.from_user.id].append(msg.text)
        bot.send_message(msg.from_user.id, 'Введите второе число.')
        bot.send_message(msg.from_user.id, f'{dct}')
        dct[msg.from_user.id][0] = 3

    elif dct[msg.from_user.id][0] == 3:
        bot.send_message(msg.from_user.id, f'Ваш результат '
                                           f'{dct[msg.from_user.id][-1]} + '
                                           f'{msg.text}')
        bot.send_message(msg.from_user.id, f'{dct}')
        dct[msg.from_user.id] = [1]


bot.polling()
