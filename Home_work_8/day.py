import menu
import check

def choose():
    menu.print_(menu.week)
    user_select = input()
    if not check.menu_item(user_select, menu.week):
        print("Некорректный ввод")
        return choose()
    return user_select
