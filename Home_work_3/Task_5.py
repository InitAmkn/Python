
'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
Негафибоначчи
'''


def Negafibonacci_Numbers(n):
    fibonacci_lst = []

    for i in range(0, n+1):
        Fn = round((((1 + 5**0.5)/2)**i - ((1 - 5**0.5)/2)**i)/5**0.5)
        fibonacci_lst.append(Fn)
        if i != 0:
            fibonacci_lst.insert(0, Fn*((-1)**(i+1)))
    return fibonacci_lst


print(Negafibonacci_Numbers(10))
