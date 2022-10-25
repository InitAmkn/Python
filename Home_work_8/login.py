def input_login(menu):
    output_list = []
    for i in range(len(menu)):
        print(menu[i], end=" ")
        output_list.append(input())
    return output_list