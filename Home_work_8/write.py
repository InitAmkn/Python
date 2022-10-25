def list_in_file_persons(list=[]):
    with open("Home_work_8/data/persons.CSV", "a", encoding="UTF-8") as data_file:
        data_file.write(";".join(list))
        data_file.write("\n")


def add_lesson(list=[]):
    with open("Home_work_8/data/schedule.CSV", "a", encoding="UTF-8") as data_file:
        data_file.write(";".join(list))
        data_file.write("\n")


def overwriting(list=[]):
    with open("Home_work_8/data/schedule.CSV", "w", encoding="UTF-8") as data_file:
        for i in list:
            data_file.write(";".join(i))
            data_file.write("\n")
