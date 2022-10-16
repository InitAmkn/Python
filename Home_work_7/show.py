

def all_empty():
    persons = []
    with open("Home_work_7/Telephone directory.txt", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())
    persons = [persons[i].replace("\n", "").split(" ")
               for i in range(len(persons))]
    print("---------------")
    for i in range(len(persons)):
        print(f"Имя:     {persons[i][0]}")
        print(f"Фамилия: {persons[i][1]}")
        print(f"Телефон: {persons[i][2]}")
        print(f"Описание:{persons[i][3]}")
        print("---------------")
