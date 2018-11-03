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

def main():
    bag = [i for i in range(1,91)]
    player_card = create_card(bag)
    computer_card = create_card(bag)


if __name__ == '__main__':
    main()