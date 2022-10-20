

def format_1(way):
    with open(way + "/format_1.txt", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())

    persons = [persons[i].replace("\n", "").split(";")
               for i in range(len(persons))]
    write(persons)


def format_2(way):
    with open(way + "/format_2.txt", "r", encoding="UTF-8") as data_file:
        persons = str(data_file.read())
    sep_1 = "~"
    sep_2 = ";"
    persons = persons.replace("\n\n", sep_1)
    persons = persons.replace("\n", sep_2)
    if persons[-1] == sep_1:
        persons = persons[:-1]
    if persons[-1] == sep_2:
        persons = persons[:-1]

    persons = persons.split(sep_1)
    persons = [persons[i].split(sep_2)
               for i in range(len(persons))]
    write(persons)


def write(persons):
    with open("Home_work_7/Telephone directory.txt", "a", encoding="UTF-8") as data_file:
        for i in persons:
            data_file.writelines(' '.join(i))
            data_file.write("\n")
