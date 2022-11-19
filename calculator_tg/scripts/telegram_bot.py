
from telebot import types
from telebot import TeleBot
import log
import datetime

bot = TeleBot('')

value = ''
old_value = ''


keyboard = types.InlineKeyboardMarkup()
keyboard.row(types.InlineKeyboardButton("j", callback_data="j"),
             types.InlineKeyboardButton("C", callback_data="C"),
             types.InlineKeyboardButton("<=", callback_data="<="),
             types.InlineKeyboardButton("/", callback_data="/"),
             )
keyboard.row(types.InlineKeyboardButton("7", callback_data="7"),
             types.InlineKeyboardButton("8", callback_data="8"),
             types.InlineKeyboardButton("9", callback_data="9"),
             types.InlineKeyboardButton("*", callback_data="*"),
             )
keyboard.row(types.InlineKeyboardButton("4", callback_data="4"),
             types.InlineKeyboardButton("5", callback_data="5"),
             types.InlineKeyboardButton("6", callback_data="6"),
             types.InlineKeyboardButton("-", callback_data="-"),)

keyboard.row(types.InlineKeyboardButton("1", callback_data="1"),
             types.InlineKeyboardButton("2", callback_data="2"),
             types.InlineKeyboardButton("3", callback_data="3"),
             types.InlineKeyboardButton("+", callback_data="+"),)

keyboard.row(types.InlineKeyboardButton(" ", callback_data="no"),
             types.InlineKeyboardButton("0", callback_data="0"),
             types.InlineKeyboardButton(",", callback_data="."),
             types.InlineKeyboardButton("=", callback_data="="),)


@bot.message_handler(commands=['help'])
def get_message(message):
    global value
    bot.send_message(message.from_user.id,
                     "Доступные функции: ")
    bot.send_message(message.from_user.id,
                     "/start")
    bot.send_message(message.from_user.id,
                     "/history")


@bot.message_handler(commands=['start'])
def get_message(message):
    global value
    bot.send_message(message.from_user.id,
                     "Привет, это калькулятор комплексных и обычных чисел:")
    if value == "":
        bot.send_message(message.from_user.id,
                         "Введите выражение", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,
                         value, reply_markup=keyboard)


@bot.message_handler(commands=['history'])
def get_message(message):
    bot.send_message(message.from_user.id,
                     f"{message.from_user.first_name} вот история ваших запросов: ")
    cash = log.read()
    show_cash = ["; ".join(cash[i][2:]) for i in range(
        len(cash)) if cash[i][0] == str(message.from_user.id)]
    show_cash = "\n ".join(show_cash)

    bot.send_message(message.from_user.id,
                     f"{show_cash}")


@ bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    if data == "no":
        pass
    elif data == "C":
        value = ""
    elif data == "=":
        if len(value) > 0 and not value[-1].isdigit() and value[-1] != "j":
            value = value[:-1]
        save = str(value)
        value = str(eval(value))
        value = value.replace("(", "").replace(")", "")
        save = save + " = " + str(value)
        log.write([str(query.from_user.id), str(
            datetime.datetime.now()), save])
        save = ""

    elif data == "<=":
        value = value[:-1]

    elif data == ".":
        if value == "":
            value = "0"+data
        if len(value) > 0:
            if not value[-1].isdigit() and value[-1] != data and value[-1] != "j":
                value += "0"+data
            count = 0
            i = len(value)-1
            while (value[i].isdigit() or value[i] == data) and i >= 0:
                if value[i] == data:
                    count += 1
                i -= 1
            if count > 0 or value[-1] == "j":
                pass
            else:
                value += data

    elif not data.isdigit() and len(value) > 0 and not value[-1].isdigit() and value[-1] != "j":
        pass

    elif data.isdigit() and len(value) > 0 and value[-1] == "j":
        pass
    else:
        value += data
    if value != old_value:
        if value == "":
            bot.edit_message_text(
                chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.message_id, text=value, reply_markup=keyboard)
    old_value = value


bot.polling(none_stop=False, interval=0)
