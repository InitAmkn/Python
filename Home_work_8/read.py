def file_persons():
    with open("Home_work_8/data/persons.CSV", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())
        persons = [persons[i].replace("\n", "").split(";")
                   for i in range(len(persons))]
        return persons


def file_schedule():
    with open("Home_work_8/data/schedule.CSV", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())
        persons = [persons[i].replace("\n", "").split(";")
                   for i in range(len(persons))]
        return persons


def find_persons(login):
    persons = file_persons()
    for i in range(len(persons)):
        if login == persons[i][0]:
            return persons[i]
