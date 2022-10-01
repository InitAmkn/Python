'''
2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
'''

a = ["123", "234", 123, "567", 'werwer', 33, '324', 'werwww']
value = 567


for i in range(len(a)):
    if type(a[i]) == int:
        if a[i] == value:
            print(f'Value found on position {i}')
            break
    elif type(a[i]) == str:
        if a[i].isdigit() and int(a[i]) == value:
            print(f'Value found on position {i}')
            break
else:
    print('Value not found')
