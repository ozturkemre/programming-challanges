def play(n=None):
    if n is None:
        while True:
            try:
                n = int(input('Input the grid size: '))
            except ValueError:
                print('Invalid input')
                continue
            if n <= 0:
                print('Invalid input')
                continue
            break

    grids = [[0]*n for _ in range(n)]
    user = 1
    print('Current board:')
    print(*grids, sep='\n')
    while True:
        user_input = get_input(user, grids, n)
        place_piece(user_input, user, grids)
        print('Current board:')
        print(*grids, sep='\n')


        if check_won(user_input, user, n, grids):
            print('Player', user, 'has won')
            return

        if not any(0 in grid for grid in grids):
            return

        user = 2 if user == 1 else 1


def get_input(user, grids, n):
    instr = 'Input a slot player {0} from 1 to {1}: '.format(user, n)
    while True:
        try:
            user_input = int(input(instr))
        except ValueError:
            print('invalid input:', user_input)
            continue
        if 0 > user_input or user_input > n+1:
            print('invalid input:', user_input)
        elif grids[0][user_input-1] != 0:
            print('slot', user_input, 'is full try again')
        else:
            return user_input-1


def place_piece(user_input, user, grids):
    for grid in grids[::-1]:
        if not grid[user_input]:
            grid[user_input] = user
            return


# def check_won(user_input, user, n, grids):
#     column = [i[user_input] for i in grids]
#     print("column")
#     print(column)
#     if grids[user_input].count(user) == 4:
#         print("aaaa"+ grids[user_input])
#         return True
#     index = 0
#     for i in column:
#         if i == 0:
#             index += 1
#             print(index)
#     print("index: "+str(index))
#     if column.count(user) == 4:
#         return True



#play()