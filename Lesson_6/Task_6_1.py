
'''
1. Напишите программу вычисления арифметического выражения заданного строкой. 
   Используйте операции +,-,/,*. приоритет операций стандартный. 
    *Пример:* 
    2+2 => 4; 
    1+2*3 => 7; 
    1-2*3 => -5;
'''
'''
s = '10*55+21*2'

lst = []
last = -1
for i in range(len(s)):
    if s[i] in {'+', '-', '*', '/'}:
        lst.append(s[last + 1:i])
        lst.append(s[i])
        last = i
lst.append(s[last + 1])
print(lst)

s = lst

lst_res = [int(s[0])]
i = 1
while i < len(s):
    if s[i] == '+':
        lst_res.append(int(s[i + 1]))
    elif s[i] == '-':
        lst_res.append(-int(s[i + 1]))
    elif s[i] == '*':
        lst_res[-1] = lst_res[-1] * int(s[i + 1])
    elif s[i] == '/':
        lst_res[-1] = lst_res[-1] / int(s[i + 1])
    i += 2

print(lst_res)
print(sum(lst_res))
'''
operation = "2+2*2/4"
operation = operation.replace(" ", "")


def minus(lst):
    return lst[0] - lst[1]


def multi(lst):
    return lst[0] * lst[1]


def divide(lst):
    return lst[0] / lst[1]


def count_from_string(operation):
    if "(" in operation:
        bk1 = operation.rindex("(")
        bk2 = operation.index(")", bk1)
        return count_from_string(operation[:bk1] + str(count_from_string(operation[bk1 + 1:bk2])) + operation[bk2 + 1:])
    if operation.isdigit():
        return int(operation)
    if "+" in operation:
        return sum([count_from_string(item) for item in operation.split("+", 1)])
    if "-" in operation:
        return minus([count_from_string(item) for item in operation.split("-", 1)])
    if "/" in operation:
        return divide([count_from_string(item) for item in operation.split("/", 1)])
    if "*" in operation:
        return multi([count_from_string(item) for item in operation.split("*", 1)])


print(count_from_string(operation))

'''
2 Добавьте возможность использования скобок, меняющих приоритет операций.
        *Пример:* 
        1+2*3 => 7; 
        (1+2)*3 => 9;
        
'''

'''
3. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

    [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''
