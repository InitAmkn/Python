def write(list=[]):
    with open("calculator_tg/data/log.CSV", "a", encoding="UTF-8") as data_file:
        data_file.write(";".join(list))
        data_file.write("\n")


def read():
    with open("calculator_tg/data/log.CSV", "r", encoding="UTF-8") as data_file:
        operations = list(data_file.readlines())
        operations = [operations[i].replace("\n", "").split(";")
                      for i in range(len(operations))]
        return operations
