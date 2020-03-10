import copy
import os
import random
import time

from termcolor import cprint


def reset():
    print("""
    MAIN MENU
    =========
    
    
    ->How to play, type 'i'
    ->Play, type 'p'
    """)

    choice = input(": ")
    if choice == 'i':
        os.system('clear')
        # Prints instruction file.
        print(open('instructions.txt', 'r').read())
    elif choice != 'p':
        os.system("clear")
        reset()

    # The solution grid
    b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(0, 10):
        place_mine(b)
    for r in range(0, 9):
        for c in range(0, 9):
            value = get_value(r, c, b)
            if value == '*':
                update_values(r, c, b)
    k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    print_board(k)
    start_time = time.time()
    play(b, k, start_time)


def get_value(r, c, b):
    return b[r][c]


# Place a mine in a random location
def place_mine(m):
    r = random.randint(0, 8)
    c = random.randint(0, 8)
    # Checks if there is a bomb
    current_row = m[r]
    if not current_row[c] == '*':
        current_row[c] = '*'
    else:
        place_mine(m)


def update_values(rn, c, b):
    # row above.top left, top, top right
    if rn - 1 > -1:
        r = b[rn - 1]

        if c - 1 > 1:
            if not r[c - 1] == '*':
                r[c - 1] += 1
        if not r[c] == '*':
            r[c] += 1
        if 9 > c + 1:
            if not r[c + 1] == '*':
                r[c + 1] += 1
    # same row. left and right cell
    r = b[rn]
    if c - 1 > -1:
        if not r[c - 1] == '*':
            r[c - 1] += 1

    if 9 > c + 1:
        if not r[c + 1] == '*':
            r[c + 1] += 1

    # Row below. bottom left, bottom, bottom right
    if 9 > rn + 1:
        r = b[rn + 1]

        if c - 1 > -1:
            if not r[c - 1] == '*':
                r[c - 1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c + 1:
            if not r[c + 1] == '*':
                r[c + 1] += 1


def zero_blow(r, c, k, b):
    # row above.top left, top, top right
    if r - 1 > -1:
        row = k[r - 1]
        if c - 1 > -1:
            row[c - 1] = get_value(r - 1, c - 1, b)
        row[c] = get_value(r - 1, c, b)
        if 9 > c + 1:
            row[c + 1] = get_value(r - 1, c + 1, b)

    # same row. left and right cell
    row = k[r]
    if c - 1 > -1:
        row[c - 1] = get_value(r, c - 1, b)
    if 9 > c + 1:
        row[c + 1] = get_value(r, c + 1, b)

    # Row below. bottom left, bottom, bottom right
    if 9 > r + 1:
        row = k[r + 1]
        if c - 1 > -1:
            row[c - 1] = get_value(r + 1, c - 1, b)
        row[c] = get_value(r + 1, c, b)
        if 9 > c + 1:
            row[c + 1] = get_value(r + 1, c + 1, b)


def check_around(k, b, r, c):
    old = copy.deepcopy(k)
    zero_blow(r, c, k, b)
    if old == k:
        return
    while True:
        old = copy.deepcopy(k)
        for x in range(9):
            for y in range(9):
                if get_value(x, y, k) == 0:
                    zero_blow(x, y, k, b)
        if old == k:
            return


def marker(r, c, k):
    k[r][c] = '⚐'
    print_board(k)


def print_board(b):
    os.system("clear")
    print('    A   B   C   D   E   F   G   H   I')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
    for r in range(0, 9):
        print(r, '║', get_value(r, 0, b), '║', get_value(r, 1, b), '║', get_value(r, 2, b), '║',
              get_value(r, 3, b), '║', get_value(r, 4, b), '║', get_value(r, 5, b), '║', get_value(r, 6, b), '║',
              get_value(r, 7, b), '║', get_value(r, 8, b), '║')
        if r != 8:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')


def choose(b, k, start_time):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    while True:
        chosen = input('Choose a square (eg. E4) or place a marker (eg. mE4): ').lower()
        if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
            c, r = (ord(chosen[1])) - 97, int(chosen[2])
            marker(r, c, k)
            play(b, k, start_time)
            break
        elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers:
            return (ord(chosen[0])) - 97, int(chosen[1])
        else:
            choose(b, k, start_time)


def play(b, k, start_time):
    # Player chooses square
    c, r = choose(b, k, start_time)
    # Gets the value at that location.
    v = get_value(r, c, b)
    # if there is a mine
    if v == '*':
        print_board(b)
        print("Yo lose!")
        # Print timer result.
        print('Time: ' + str(round(time.time() - start_time)) + 's')
        play_again = input('Play again? (Y/N): ')
        if play_again == 'y':
            os.system("clear")
            reset()
        else:
            quit()
    # Puts that value into the known grid (k).
    k[r][c] = v
    if v == 0:
        check_around(k, b, r, c)
    print_board(k)
    squares_left = 0
    for x in range(0, 9):
        row = k[x]
        squares_left += row.count(' ')
        squares_left += row.count('⚐')
    if squares_left == 10:
        print_board(b)
        print('You win!')
        # Print timer result.
        print('Time: ' + str(round(time.time() - start_time)) + 's')
        play_again = input('Play again? (Y/N): ')
        play_again = play_again.lower()
        if play_again == 'y':
            os.system("clear")
            reset()
        else:
            quit()
    play(b, k, start_time)


# Introduction
cprint("Welcome to MineSweeper v.1.0", "blue")
cprint("============================", "red")

reset()
