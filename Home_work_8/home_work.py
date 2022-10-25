import menu
import write
import read
import check
import day as day_now


def editing_controller(day=""):
    if day == "":
        day = day_now.choose()
    menu.print_(menu.home_work_editing)
    user_select = input()
    if not check.menu_item(user_select, menu.home_work_editing):
        print("Некорректный ввод")
        return editing_controller(day)
    if user_select == menu.home_work_editing[1][0]:
        add(day)
    if user_select == menu.home_work_editing[2][0]:
        remove(day)
    if user_select == menu.home_work_editing[3][0]:
        editing_controller()


def remove(day):
    add(day, True)


def add(day, remove=False):
    schedule = read.file_schedule()
    not_contain_day = [schedule[i]
                       for i in range(len(schedule)) if schedule[i][0] != day]
    contain_day = [schedule[i]
                   for i in range(len(schedule)) if schedule[i][0] == day]

    print(f"Расписание на день недели: {menu.week[int(day)][1]}")
    print()
    for i in range(len(contain_day)):
        print(f"{i+1}. ", "\t Дз -".join(contain_day[i][1:]))
    print()

    if len(contain_day) > 0:
        input_index = False
        while not input_index:
            try:
                index = int(input(f"Выберите № урока:"))
                input_index = True

            except:
                input_index = False
                print("Пожалуйста повторите попытку")
    else:
        print("В расписании на данный день нет занятий")
        print()
        return editing_controller()

    if not remove:
        print("Введите ДЗ:")
        home_work = ""
        home_work = input(f"{contain_day[index-1][1]} :")

    if not remove and len(contain_day[index-1]) < 3:
        contain_day[index-1].append(home_work)
        print("Дз записано")
    elif not remove and len(contain_day[index-1]) > 2:
        contain_day[index-1] = contain_day[index-1][:2]
        contain_day[index-1].append(home_work)
        print("Дз успешно перезаписано")

    if remove and len(contain_day[index-1]) > 2:
        contain_day[index-1] = contain_day[index-1][:2]
        print("Дз успешно удалено")
    elif remove and len(contain_day[index-1]) < 3:
        print("Нечего удалять")

    schedule = not_contain_day + contain_day
    write.overwriting(schedule)
