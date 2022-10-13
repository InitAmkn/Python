'''3. Создайте программу для игры в ""Крестики-нолики"".'''


def print_list(map_):
    for i in range(len(map_)):
        print(map_[i])


def create_map(n):
    map_ = []
    for i in range(n):
        map_line = []
        for j in range(n):
            map_line.append(str(i)+str(j))
        map_.append(map_line)
    return map_


def check_win(player, map_):
    if map_[0][0] == player:
        win = True
        for i in range(len(map_)):
            if map_[i][i] != player:
                win = False
        if win:
            return win

    if map_[0][len(map_)-1] == player:
        win = True
        for i in range(len(map_)):
            if map_[len(map_)-i-1][i] != player:
                win = False
        if win:
            return win

    for i in range(len(map_)):
        win = True
        for j in range(len(map_)):
            if map_[i][j] != player:
                win = False
        if win:
            return True

    for j in range(len(map_)):
        win = True
        for i in range(len(map_)):
            if map_[i][j] != player:
                win = False
        if win:
            return True
    return False


def drawn_game(map_):
    drawn = True
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] != "X" and map_[i][j] != "O":
                drawn = False
    return drawn


def tic_tac_toe(map_):
    print_list(map_)
    player = "O"
    while not check_win(player, map_):
        if player == "X":
            player = "O"
        elif player == "O":
            player = "X"
        x = input(f"Введите координату для {player}: ")
        can_add = False
        while not can_add:
            for i in range(len(map_)):
                for j in range(len(map_)):
                    if map_[i][j] == x and x != "X" and x != "O":
                        temp_i = i
                        temp_j = j
                        can_add = True
                        break
            if not can_add:
                print("Некорректный ввод")
                x = input(f"Введите координату для {player}: ")
        else:
            map_[temp_i][temp_j] = player
            print_list(map_)
        if drawn_game(map_) == True:
            print("НИЧЬЯ")
            break
    else:
        print(f"Победил: {player}")


map_ = create_map(3)
tic_tac_toe(map_)
