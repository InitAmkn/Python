import menu
import add
import show


while (True):
    menu.print_menu()
    n = input("Выберите № действия: ")

    if n == "1":
        show.all_empty()
    elif n == "2":
        add.new_empty()
    elif n == "7":
        break
    else:
        print("Некорректный ввод")
