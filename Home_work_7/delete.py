
def empty():
    try:
        delete_i = int(input("Введите № удаляемой персоны: "))
    except:
        print("Введите число")
        empty()
    with open("Home_work_7/Telephone directory.txt", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())
    persons = [persons[i].replace("\n", "").split(" ")
               for i in range(len(persons)) if i != delete_i]
    overwriting(persons)


def overwriting(persons):
    with open("Home_work_7/Telephone directory.txt", "w", encoding="UTF-8") as data_file:
        for i in persons:
            data_file.writelines(' '.join(i))
            data_file.write("\n")
