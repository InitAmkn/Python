from turtle import home
import write
import entry
import menu
import check
import read
import show
import lessons
import home_work


def controller(data_person):
    print()
    print(
        f"Здравствуйте, {menu.status[int(data_person[2])][1]} {data_person[0]}")
    print()

    menu.print_(menu.main, menu.access_modifier[int(data_person[2])-1][1:])
    user_select = input()
    if not check.menu_item(user_select, menu.main, menu.access_modifier[int(data_person[2])-1][1:]):
        print("Некорректный ввод")
        return controller(data_person)

    if user_select == menu.main[1][0]:
        show.schedule()
        return controller(data_person)

    if user_select == menu.main[2][0]:
        home_work.editing_controller()
        return controller(data_person)

    if user_select == menu.main[3][0]:
        lessons.editing_controller()
        return controller(data_person)

    if user_select == menu.main[4][0]:
        return controller(entry.option())


controller(entry.option())


''' 
    if user_select == menu.main[2][0]:
        show_schedule()
    if user_select == menu.main[3][0]:

    if user_select == menu.main[4][0]:
'''
