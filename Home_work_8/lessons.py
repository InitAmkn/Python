import menu
import write
import read
import check
import day as day_now


def editing_controller(day=""):
    if day == "":
        day = day_now.choose()
    menu.print_(menu.lesson_editing)
    user_select = input()
    if not check.menu_item(user_select, menu.lesson_editing):
        print("Некорректный ввод")
        return editing_controller(day)
    if user_select == menu.lesson_editing[1][0]:
        add(day)
    if user_select == menu.lesson_editing[2][0]:
        remove(day)
    if user_select == menu.lesson_editing[3][0]:
        editing_controller()


def remove(day):
    schedule = read.file_schedule()
    not_contain_day = [schedule[i]
                       for i in range(len(schedule)) if schedule[i][0] != day]
    contain_day = [schedule[i]
                   for i in range(len(schedule)) if schedule[i][0] == day]
    print(f"Расписание на день недели: {menu.week[int(day)][1]}")
    print()
    for i in range(len(contain_day)):
        print(f"{i+1}. {contain_day[i][1]}")
    print()

    if len(contain_day) > 0:
        while True:
            try:
                del_index = int(input(f"Выберите № урока для удаления:"))
                if del_index > 0:
                    contain_day.pop(del_index-1)
                    break
            except:
                print("Пожалуйста повторите попытку")
            print("Пожалуйста повторите попытку")
        schedule = not_contain_day + contain_day
        write.overwriting(schedule)
    else:
        print("В расписании на данный день нет занятий")
        print()
    editing_controller(day)


def add(day):
    print(f"Расписание на день недели: {menu.week[int(day)][1]}")
    schedule = read.file_schedule()

    count_lesson = 1
    for i in schedule:
        if day == i[0]:
            count_lesson += 1

    lesson = input(f"Введите наименование {count_lesson} урока:")
    write.add_lesson([day, lesson])
    editing_controller(day)
