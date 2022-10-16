

list_menu = [['1', 'Просмотр записей'],
             ['2', 'Добавление записи'],
             ['3', 'Экспорт из файла'],
             ['4', 'Импорт в файл'],
             ['5', 'Выход из программы'],
             ['6', 'Поиск записи'],
             ['7', 'Удаление записи']]


def print_menu(list_menu):
    print("Меню:\n")
    for i in range(len(list_menu)):
        print(end='\t')
        for j in range(len(list_menu[i])):
            print(list_menu[i][j], end=' ')
        print()
    print()


def user_selection():
    continue_work = True
    while (continue_work):
        print_menu(list_menu)
        n = input("Выберите действие: ")
