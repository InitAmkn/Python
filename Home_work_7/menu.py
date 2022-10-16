

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


def user_selection(choice):
    for i in range(len(menu)):
        if choice == menu[i][0]:
            return choice
