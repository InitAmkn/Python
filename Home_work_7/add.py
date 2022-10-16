

def new_empty():
    data_person = (input("Имя:     "),
                   input("Фамилию: "),
                   input("Телефон: "),
                   input("Описание:"))

    with open("Home_work_7/Telephone directory.txt", "a", encoding="UTF-8") as data_file:
        data_file.writelines(' '.join(data_person))
        data_file.writelines("\n")
    print("---------------")
