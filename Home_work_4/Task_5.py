
'''
5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.
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


def creating_random_polynomials(n):
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
                polynomial.append(f"{sign}{b}*x{degree_x[i]}")
            if i == 1:
                polynomial.append(f"{sign}{b}*x")
            if i == 0:
                polynomial.append(f"{sign}{b}")
    polynomial_str = ''.join(polynomial)
    if polynomial_str[0] == '+':
        polynomial_str = polynomial_str[1:]
    return polynomial_str


def multiplier_list(big_string):
    x = []
    big_string = big_string.replace('\n', '*x\u2070')
    big_string = big_string.replace('-', '+-')
    big_string = big_string.replace('++', '+')
    # print(big_string)
    big_string = big_string.split("+")
    for k in range(len(big_string)):
        x.append(big_string[k].split('*'))
    num_list = []
    for i in range(len(x)):
        num_list.append([int(x[i][0]), x[i][1]])
    return num_list


def group_by(num_list):
    num_list_1 = []
    cash = []
    for i in range(len(num_list)):
        if num_list[i][1] not in cash:
            current_num = num_list[i]
            for k in range(i+1, len(num_list)):
                if num_list[i][1] == num_list[k][1]:
                    current_num[0] += num_list[k][0]
            num_list_1.append([current_num[0], num_list[i][1]])
            cash.append(num_list[i][1])
    return num_list_1


def creating_polynomials(n):
    polynomial = []
    for i in range(len(n)):
        b = n[i][0]
        sign = ""
        if b > 0:
            sign = "+"
        else:
            sign = ""
        if b != 0:
            polynomial.append(f"{sign}{b}*{n[i][1]}")
    polynomial_str = ''.join(polynomial).replace("*x⁰", "")
    if polynomial_str[0] == '+':
        polynomial_str = polynomial_str[1:]
    return polynomial_str


'''for i in range(10):
    with open("Home_work_4/Task 5_1.txt", "a", encoding="UTF-8") as data_file:
        data_file.write(f"{creating_random_polynomials(randint(0, 9))}\n")
    with open("Home_work_4/Task 5_2.txt", "a", encoding="UTF-8") as data_file:
        data_file.write(f"{creating_random_polynomials(randint(0, 9))}\n")'''

with open("Home_work_4/Task 5_1.txt", "r", encoding="UTF-8") as data_file:
    file_1 = list(data_file.readlines())
with open("Home_work_4/Task 5_2.txt", "r", encoding="UTF-8") as data_file:
    file_2 = list(data_file.readlines())

big_string = '+'.join(file_1) + '+' + '+'.join(file_2)

# print(GroupBy(multiplier_list(big_string)))
# print(creating_polynomials(GroupBy(multiplier_list(big_string))))

with open("Home_work_4/Task 5_3_sum.txt", "a", encoding="UTF-8") as data_file:
    data_file.write(
        f"{creating_polynomials(group_by(multiplier_list(big_string)))}\n")


'''polinom_1 = '5*x^2 + 3*x^6 - 15*x**3 + 66'
polinom_2 = '13*x^3 + 3*x^4 - 15*x^8 - 99'
 
polinom_1 = polinom_1.replace(' ', '').replace('**', '^').replace('*', '')
polinom_2 = polinom_2.replace(' ', '').replace('**', '^').replace('*', '')
 
 
def get_dict_from_polinom(str_pol):
    lst = []
    last_index = -1
    neg = False
    for i, char in enumerate(str_pol):
        if char == '+' or char == '-':
            if neg:
                lst.append('-' + str_pol[last_index + 1:i])
            else:
                lst.append(str_pol[last_index + 1:i])
            last_index = i
            neg = char == '-'
    if neg:
        lst.append('-' + str_pol[last_index + 1:])
    else:
        lst.append(str_pol[last_index + 1:])
 
    print(lst)
    dct = {}
    for item in lst:
        for i, char in enumerate(item):
            if not char.isdigit() and char != '.' and char != '-':
                dct[item[i:]] = float(item[:i])
                break
        else:
            dct[''] = float(item)
 
    return dct
 
 
dct1 = get_dict_from_polinom(polinom_1)
dct2 = get_dict_from_polinom(polinom_2)
 
set1 = set(dct1.keys())
set2 = set(dct2.keys())
 
itog_dct = {}
 
for key in set1.intersection(set2):
    itog_dct[key] = dct1[key] + dct2[key]
 
for key in set1.symmetric_difference(set2):
    if key in dct1:
        itog_dct[key] = dct1[key]
    else:
        itog_dct[key] = dct2[key]
 
 
print(itog_dct)
 
print([f'{itog_dct[key]}{key}' for key in sorted(itog_dct.keys(), reverse=True)])'''
