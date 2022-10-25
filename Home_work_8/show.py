import menu
import read


def schedule():
    schedule = read.file_schedule()
    schedule.sort(key=lambda x: x[0])

    for i in range(1, len(menu.week)):
        print(f"{menu.week[i][1]}")
        num_lesson = 1
        for j in range(1, len(schedule)):
            if menu.week[i][0] == schedule[j][0]:
                print(f"{num_lesson}. ", "\t ДЗ: ".join(schedule[j][1:]))
                num_lesson += 1
        num_lesson = 0
        print()
