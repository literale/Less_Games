import random

def print_field(game_field):
    line_one = '|'.join(game_field[0:3])
    line_two = '|'.join(game_field[3: 6])
    line_three = '|'.join(game_field[6: 9])
    print(line_one)
    print(line_two)
    print(line_three)
    print("\n")

def player_move(cell, done_cell, game_field, not_done_cell):
    if (done_cell.count(cell)!=0):
        print("Не читери!")
    elif cell< 0 or cell > 8:
        print("Такой клетки нет!")
    else:
        done_cell.append(cell)
        game_field[cell]="_o_"
        not_done_cell.remove(cell)

def computer_move(not_done_cell, game_field, done_cell):
    cell = random.choice(not_done_cell)
    done_cell.append(cell)
    not_done_cell.remove(cell)
    game_field[cell] = "_x_"

def win_or_not(run, game_field, done_cell):
    if game_field[0] == "_x_" and game_field[1] == "_x_" and game_field[2] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[0] == "_o_" and game_field[1] == "_o_" and game_field[2] == "_o_":
        print("Вы победили!")
        run = False

    if game_field[3] == "_x_" and game_field[4] == "_x_" and game_field[5] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[3] == "_o_" and game_field[4] == "_o_" and game_field[5] == "_o_":
        print("Вы победили!")
        run = False

    if game_field[6] == "_x_" and game_field[7] == "_x_" and game_field[8] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[6] == "_o_" and game_field[7] == "_o_" and game_field[8] == "_o_":
        print("Вы победили!")
        run = False

    if game_field[0] == "_x_" and game_field[3] == "_x_" and game_field[6] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[0] == "_o_" and game_field[3] == "_o_" and game_field[6] == "_o_":
        print("Вы победили!")
        run = False

    if game_field[1] == "_x_" and game_field[4] == "_x_" and game_field[7] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[1] == "_o_" and game_field[4] == "_o_" and game_field[7] == "_o_":
        print("Вы победили!")
        run = False

    if game_field[2] == "_x_" and game_field[5] == "_x_" and game_field[8] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[2] == "_o_" and game_field[5] == "_o_" and game_field[8] == "_o_":
        print("Вы победили!")
        run = False

    if game_field[0] == "_x_" and game_field[4] == "_x_" and game_field[8] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[0] == "_o_" and game_field[4] == "_o_" and game_field[8] == "_o_":
        print("Вы победили!")
        run = False

    if game_field[2] == "_x_" and game_field[4] == "_x_" and game_field[6] == "_x_":
        print("Компьютер победил!")
        run = False
    if game_field[2] == "_o_" and game_field[4] == "_o_" and game_field[6] == "_o_":
        print("Вы победили!")
        run = False

    if(len(done_cell)==9) and run == True:
        run = False
        print("Ничья!")
    return run


def main():
    game_field = ["_0_","_1_","_2_","_3_","_4_","_5_","_6_","_7_","_8_"]
    print_field(game_field)
    run = True
    done_cell = []
    not_done_cell = [0,1,2,3,4,5,6,7,8]
    i = 0
    while run:
        cell = int(input("Куда вы хотите поставить о?\n"))
        player_move(cell, done_cell, game_field, not_done_cell)
        print_field(game_field)
        run =  win_or_not(run, game_field, done_cell)
        computer_move(not_done_cell, game_field, done_cell)
        print_field(game_field)
        run = win_or_not(run, game_field, done_cell)


if __name__ == '__main__':
    main()
