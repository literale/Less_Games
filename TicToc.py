import random

def player_input(done_cell, not_done_cell):
    for i in range (10):
        cell = int(input("Куда вы хотите поставить о?\n"))
        if (done_cell.count(cell)!=0):
            print("Не читери!")
        elif cell< 0 or cell > 8:
            print("Такой клетки нет!")
        else:
            break
        if i == 9:
            print("Попытки истекли! Будет выбрана случайная клетка!")
            return random.choice(not_done_cell)
    return cell


def print_field(game_field):
    line_one = '|'.join(game_field[0:3])
    line_two = '|'.join(game_field[3: 6])
    line_three = '|'.join(game_field[6: 9])
    print(line_one)
    print(line_two)
    print(line_three)
    print("\n")

def player_move(cell, done_cell, game_field, not_done_cell):
        done_cell.append(cell)
        game_field[cell]="_o_"
        not_done_cell.remove(cell)

def computer_move(not_done_cell, game_field, done_cell):
    cell = random.choice(not_done_cell)
    done_cell.append(cell)
    not_done_cell.remove(cell)
    game_field[cell] = "_x_"

def win_or_not(run, game_field, done_cell):
    for i in range (0,6,3):
        if game_field[i] == game_field[i+1] and game_field[i+1]== game_field[i+2]:
            run = False
            if game_field[i] == "_o_":
                print("Вы победили!")
            else:
                print("Компьютер победил!")
    for i in range (3):
        if game_field[i] == game_field[i+3] and game_field[i+3] == game_field[i+6]:
            run = False
            if game_field[i] == "_o_":
                print("Вы победили!")
            else:
                print("Компьютер победил!")

    if game_field[0] == game_field[4] and game_field[4] == game_field[8]:
        run = False
        if  game_field[0] == "_o_":
            print("Вы победили!")
        else: print("Компьютер победил!")

    elif game_field[2] == game_field[4] and game_field[4] == game_field[6]:
        run = False
        if  game_field[2] == "_o_":
            print("Вы победили!")
        else: print("Компьютер победил!")

    elif(len(done_cell)==9) and run == True:
        run = False
        print("Ничья!")
    return run


def main():
    game_field = ["_0_","_1_","_2_","_3_","_4_","_5_","_6_","_7_","_8_"]
    print_field(game_field)
    run = True
    done_cell = []
    not_done_cell = [0,1,2,3,4,5,6,7,8]

    while run:
        #cell = int(input("Куда вы хотите поставить о?\n"))
        #player_move(cell, done_cell, game_field, not_done_cell)
        cell = player_input(done_cell, not_done_cell)
        player_move(cell, done_cell, game_field, not_done_cell)
        print_field(game_field)
        run =  win_or_not(run, game_field, done_cell)
        if (run == False):
            break
        computer_move(not_done_cell, game_field, done_cell)
        print_field(game_field)
        run = win_or_not(run, game_field, done_cell)


if __name__ == '__main__':
    main()
