'''Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP'''
'''3. Создайте программу для игры в ""Крестики-нолики"".'''


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

