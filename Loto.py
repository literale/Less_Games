"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random

def create_card(bag):
    line_one = []
    line_two = []
    line_three = []
    for _ in range(5):
        line_one.append(random.choice(bag))
        line_two.append(random.choice(bag))
        line_three.append(random.choice(bag))
    card = [line_one, line_two, line_three]
    return card

def print_card(card, message):
    print(message)
    line_one = "".join(str(card[0][0:5]))
    line_two = "".join(str(card[1][0:5]))
    line_three = "".join(str(card[2][0:5]))
    print(line_one)
    print(line_two)
    print(line_three)

def close_cell(bar, player_card, computer_card):
    for i in range (3):
        for j in range (5):
            if player_card[i][j] == bar:
                player_card[i][j] == 0
            if computer_card[i][j] == bar:
                computer_card[i][j] == 0


def win_or_not(player_card, computer_card, run):
    if sum(player_card[0])+sum(player_card[1])+sum(player_card[2]) == 0:
        print("Вы победили!")
        run = False
    if sum(computer_card[0])+sum(computer_card[1])+sum(computer_card[2]) == 0:
        print("Вы проиграли!")
        run = False
    return  run

def main():
    bag = [i for i in range(1,91)]
    player_card = create_card(bag)
    computer_card = create_card(bag)
    print_card(player_card, "Карта игрока: ")
    print_card(computer_card, "Карта компьютера: ")
    run = True
    while run :
        bar = random.choice(bag)
        bag.remove(bar)
        print(bar)
        answer_not_ex = True
        while answer_not_ex:
            answer = input("Зачеркнуть цифру? (y/n)\n")
            stop = True
            if answer == "y":
                answer_not_ex = False
                stop = True
                for i in range(3):
                    for j in range(5):
                        if player_card[i][j] == bar:
                            player_card[i][j] = 0
                            stop = False
                        if computer_card[i][j] == bar:
                            computer_card[i][j] = 0
            elif answer == "n":
                answer_not_ex = False
                stop = False
                for i in range(3):
                    for j in range(5):
                        if player_card[i][j] == bar:
                            player_card[i][j] = 0
                            stop = True
                        if computer_card[i][j] == bar:
                            computer_card[i][j] = 0

        print_card(player_card, "Карта игрока: ")
        print_card(computer_card, "Карта компьютера: ")

        if stop:
            run = False
            print("Вы проиграли!")
        else:
            run = win_or_not(player_card, computer_card, run)


if __name__ == '__main__':
    main()