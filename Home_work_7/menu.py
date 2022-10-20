import add
import show
import find
import export
import import_file
import delete

menu = [('1', 'Просмотр записей'),
        ('2', 'Добавление записи'),
        ('3', 'Экспорт в файл'),
        ('4', 'Импорт из файла'),
        ('5', 'Поиск записи'),
        ('6', 'Удаление записи'),
        ('7', 'Выход из программы')
        ]


def print_menu():
    print("Меню:\n")
    for i in range(len(menu)):
        print(end='\t')
        for j in range(len(menu[i])):
            print(menu[i][j], end=' ')
        print()
    print()


def launch():
    while (True):
        print_menu()
        n = input("Выберите № действия: ")
        if n == "1":
            show.all_empty()
        elif n == "2":
            add.new_empty()
        elif n == "3":
            export.format_1("Home_work_7/export")
            export.format_2("Home_work_7/export")
        elif n == "4":
            import_file.format_1("Home_work_7/import")
            import_file.format_2("Home_work_7/import")
        elif n == "5":
            find.empty()
        elif n == "6":
            delete.empty()
        elif n == "7":
            break
        else:
            print("Некорректный ввод")
