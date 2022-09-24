'''
3. Программа получает на вход число. Необходимо вывести список простых множителей этого числa


'''
256
a = int(input("Введите число: "))
result = []
temp_a = a

for i in range(2, a):
    while temp_a % i == 0:
        result.append(i)
        temp_a = temp_a // i

print(result)
