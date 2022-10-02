
'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''


def conversion_to_binary(number):
    number_output = ""
    while (number > 0):
        number_output = f"{number % 2}" + number_output
        number = number // 2
    return number_output


print(conversion_to_binary(45))
