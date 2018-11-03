def print_field(game_field):
    line_one = '|'.join(game_field[0:3])
    line_two = '|'.join(game_field[3: 6])
    line_three = '|'.join(game_field[6: 9])
    print(line_one)
    print(line_two)
    print(line_three)

def player_move(cell, done_cell, game_field):
    if (done_cell.count(cell)!=0):
        print("Не читери!")
    elif cell< 0 or cell > 8:
        print("Такой клетки нет!")
    else:
        done_cell.append(cell)
        game_field[cell]="_o_"




def main():
    game_field = ["_0_","_1_","_2_","_3_","_4_","_5_","_6_","_7_","_8_"]
    print_field(game_field)
    run = True
    done_cell = []
    i = 0
    while run and i<10:
        cell = int(input("Куда вы хотите поставить о?\n"))
        player_move(cell, done_cell, game_field)
        print_field(game_field)
        i+=1


if __name__ == '__main__':
    main()
