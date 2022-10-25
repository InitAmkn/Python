import menu
import check
import write
import read


def option():
    data_person = []
    menu.print_(menu.entry)
    user_select = input()
    if not check.menu_item(user_select, menu.entry):
        print("Некорректный ввод")
        return option()

    if user_select == menu.entry[1][0]:
        data_person = registration()

    if user_select == menu.entry[2][0]:
        data_person = log_in()
    return data_person


def log_in():
    data_person = []
    data_person = menu.input_(menu.login)
    if not check.login_exists(data_person[0]):
        print("Пользователя с таким логином не существует")
        return log_in()
    if not check.match_password(data_person[0], data_person[1]):
        print("Пароль не верный")
        return log_in()
    data_person = read.find_persons(data_person[0])
    return data_person


def registration():
    data_person = []
    data_person = menu.input_(menu.registration)

    if check.login_exists(data_person[0]):
        print("Пользователь с таким логином уже есть")
        return registration()

    data_person = check.correct_double_pass(data_person)
    if data_person == []:
        print("Пароли не совпадают")
        return registration()

    menu.print_(menu.status)
    status = input()
    if not check.menu_item(status, menu.status):
        print("Некорректный ввод")
        return registration()
    data_person.append(status)
    write.list_in_file_persons(data_person)
    return data_person
