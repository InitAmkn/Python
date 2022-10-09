
'''
1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
   В качестве символа-разделителя используйте пробел.
'''
string_values = input("Введите числа через пробел ")
num_list = string_values.split(' ')
print(num_list)
max = int(num_list[0])
min = int(num_list[0])
for i in range(0, len(num_list)):
    if (max < int(num_list[i])):
        max = int(num_list[i])
    if (min > int(num_list[i])):
        min = int(num_list[i])
print(f"min = {min}")
print(f"max = {max}")

'''
numbers = input("Введите строку: ")
num_list = list(map(int, numbers.split()))
print(f"min = {min(num_list)}")
print(f"max = {max(num_list)}")
'''
