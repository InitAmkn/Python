'''2. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""'''


from random import randint


def game_of_candy(total_quantity_of_candies, max_сan_get_candy=28, bot=False):

    if bot:
        player = randint(2, 3)
        if player == 2:
            player = 1
    if bot == False:
        player = randint(1, 2)

    now_candy = total_quantity_of_candies
    while now_candy > max_сan_get_candy:
        correct_input = False
        if player == 1 or player == 2:
            while correct_input == False:
                print(f">>>Количество конфет на столе: {now_candy}")
                try:
                    take_candy = int(
                        input(f"Игрок #{player} введите желаемое кол-во конфет: "))
                    if take_candy > max_сan_get_candy:
                        print(
                            f"---Пожадничал, максимум можно взять {max_сan_get_candy} конфет")
                    elif take_candy <= 0:
                        print(
                            f"---Нельзя брать меньше 1 конфеты")
                    else:
                        correct_input = True
                except:
                    print("---Некорректный ввод, прошу ввести цифры")

        if player == 3:
            take_candy = artificial_intelligence(now_candy, max_сan_get_candy)
            print(f">>>Количество конфет на столе: {now_candy}")
            print(f"Бот взял конфет: {take_candy}")

        now_candy -= take_candy
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        if bot == True and player == 2:
            player = 3
        elif player == 3:
            player = 1

    else:
        if bot == True and player == 3:
            print(f"Бот забирает оставшиеся {now_candy}")
            print(f"Человеки будут порабощены")
        if player == 1 or player == 2:
            print(f"Игрок #{player} забирает оставшиеся {now_candy}")
            print(f"Игрок #{player} победил")


def artificial_intelligence(now_candy, max_сan_get_candy):
    temp = now_candy - \
        now_candy // (max_сan_get_candy + 1)*(max_сan_get_candy + 1)
    if temp > 0:
        return temp
    else:
        return randint(1, max_сan_get_candy)


game_of_candy(57, 28)
