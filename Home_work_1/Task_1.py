'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет

'''


def is_weekends(day):
    if day > 0 and day <= 5:
        return "нет"
    elif day > 5 and day <= 7:
        return "да"
    else:
        return "некорректный ввод"


a = int(input("введите день недели:"))
print("это выходной:")
print(is_weekends(a))
