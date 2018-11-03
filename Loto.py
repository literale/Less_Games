"""Участники выбирают карточки с игровыми полями.
Выбирается ведущий, вытаскивающий бочонки и оглашающий цифры на нём.
Если участник закрывает четыре клеточки из пяти в одной строке,
то он это сообщает другим игрокам словом-комбинацией «квартира».
С этого момента ведущий может вытягивать только по одному бочонку из мешочка.
При закрытии пяти клеток с цифрами на одной строке игрок выигрывает.
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



def main():
    bag = [i for i in range(1,91)]
    player_card = create_card(bag)
    computer_card = create_card(bag)
    print_card(player_card, "Карта игрока: ")
    print_card(computer_card, "Карта компьютера: ")
    run = True
    i = 0
    while run and i < 10:
        bar = random.choice(bag)
        bag.remove(bar)
        print(bar)
        i+=1
        for i in range(3):
            for j in range(5):
                if player_card[i][j] == bar:
                    player_card[i][j] = 0
                if computer_card[i][j] == bar:
                    computer_card[i][j] = 0
        print_card(player_card, "Карта игрока: ")
        print_card(computer_card, "Карта компьютера: ")


if __name__ == '__main__':
    main()