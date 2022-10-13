

'''4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''


def RLE(big_string):
    big_string = big_string + "|"
    count = 1
    RLE_list = []
    for i in range(len(big_string)-1):

        if big_string[i] == big_string[i+1]:
            count += 1
        if big_string[i] != big_string[i+1] or count > 9:
            if count > 9:
                count -= 1
            RLE_list.append(big_string[i]+str(count))
            count = 1
    return "".join(RLE_list)


def RLE_return(RLE_string):
    output_list = []
    for i in range(1, len(RLE_string), 2):
        for j in range(int(RLE_string[i])):
            output_list.append(RLE_string[i-1])
    return "".join(output_list)


big_string = "aaaaaaaaaaaaacccccccccccccffd"
print(big_string)
print(RLE(big_string))
print(RLE_return(RLE(big_string)))
