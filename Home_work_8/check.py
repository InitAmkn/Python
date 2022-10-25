import read


def login_exists(login):
    persons = read.file_persons()
    for i in persons:
        if login == i[0]:
            return True
    return False


def match_password(login, word):
    persons = read.file_persons()
    for i in persons:
        if login == i[0]:
            if word == i[1]:
                return True
    return False


def correct_double_pass(lst):
    if lst[1] == lst[2]:
        return lst[:-1]
    return []


def menu_item(item, menu, limited_menu=[]):
    if limited_menu == []:
        limited_menu = range(1, len(menu))

    for i in limited_menu:
        if item == menu[i][0]:
            return True
    return False
