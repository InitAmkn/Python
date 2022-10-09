
'''
4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:*

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
from random import randint


degree_x = {0: "\u2070",
            1: "\u00B9",
            2: "\u00B2",
            3: "\u00B3",
            4: "\u2074",
            5: "\u2075",
            6: "\u2076",
            7: "\u2077",
            8: "\u2078",
            9: "\u2079",
            }


def creating_polynomials(n):
    polynomial = []
    for i in range(n, -1, -1):
        b = randint(-3, 4)
        sign = ""
        if b > 0:
            sign = "+"
        else:
            sign = ""
        if b != 0:
            if i != 0 and i != 1:
                polynomial.append(f"{sign}{b}*х{degree_x[i]}")
            if i == 1:
                polynomial.append(f"{sign}{b}*x")
            if i == 0:
                polynomial.append(f"{sign}{b}")
    polynomial_str = ''.join(polynomial)

    if polynomial_str[0] == '+':
        polynomial_str = polynomial_str[1:]
    return polynomial_str


with open("Home_work_4/Task 4.txt", "a", encoding="UTF-8") as data_file:
    data_file.write(f"{creating_polynomials(randint(0, 9))}\n")
