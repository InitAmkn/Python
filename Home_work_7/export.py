

def format_1(way):
    with open("Home_work_7/Telephone directory.txt", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())

    persons = [persons[i].replace("\n", "").split()
               for i in range(len(persons))]

    with open(way + "/format_1.txt", "a", encoding="UTF-8") as data_file:
        for i in range(len(persons)):
            for j in range(len(persons[i])):
                data_file.write(persons[i][j])
                if j < len(persons[i])-1:
                    data_file.write(";")
            data_file.write("\n")


def format_2(way):
    with open("Home_work_7/Telephone directory.txt", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())

    persons = [persons[i].replace("\n", "").split()
               for i in range(len(persons))]

    with open(way + "/format_2.txt", "a", encoding="UTF-8") as data_file:
        for i in range(len(persons)):
            for j in range(len(persons[i])):
                data_file.write(persons[i][j])
                data_file.write("\n")
            data_file.write("\n")
