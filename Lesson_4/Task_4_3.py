'''
3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
'''
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = num1
num4 = num2

while num1 != 0 and num2 != 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1
gcd = num1 + num2
print(abs(num3 * num4) / gcd)
