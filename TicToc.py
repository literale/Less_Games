def print_field(field):
    line_one = '|'.join(field[0:3])
    line_two = '|'.join(field[3: 6])
    line_three = '|'.join(field[6: 9])
    print(line_one)
    print(line_two)
    print(line_three)



def main():
    game_field = ["_0_","_1_","_2_","_3_","_4_","_5_","_6_","_7_","_8_"]
    print_field(game_field)
    run = true
    

if __name__ == '__main__':
    main()
