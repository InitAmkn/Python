
import show


def empty():
    something_str = input("Введите данные: ")
    with open("Home_work_7/Telephone directory.txt", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())

    persons = [persons[i].replace("\n", "")
               for i in range(len(persons))]

    found_persons = [i for i in range(
        len(persons)) if something_str in persons[i]]

    persons = [persons[i].split()
               for i in range(len(persons))]
    if len(found_persons) < 1:
        print("Совпадений не найдено")
    else:
        print("Найденные совпадения:")
        for i in found_persons:
            show.empty(i, persons)
