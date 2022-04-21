# pip install pytimedinput colorama

from pytimedinput import timedInput
import os
from random import randint
from colorama import Fore, init

def print_field():
    for cell in CELLS:
        if cell in snake_body:
            print(Fore.GREEN + 'X', end='')
        if cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print(Fore.CYAN + '#', end='')
        elif cell == apple_pos:
            print(Fore.RED + 'a', end='')
        else:
            print(' ', end='')

        if cell[0] == FIELD_WIDTH - 1:
            print('')

def update_snake():
    global eaten

    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    snake_body.insert(0, new_head)
    if not eaten: snake_body.pop(-1)
    eaten = False

def apple_collision():
    global apple_pos, eaten
    if apple_pos == snake_body[0]:
        apple_pos = place_apple()
        eaten = True

def place_apple():
    col = randint(1, FIELD_WIDTH - 2)
    row = randint(1, FIELD_HEIGHT - 2)
    while (col, row) in snake_body:
        col = randint(1, FIELD_WIDTH - 2)
        row = randint(1, FIELD_HEIGHT - 2)
    return (col, row)

init(autoreset=True)

# settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]

# snake
snake_body = [(5,FIELD_HEIGHT//2), (4,FIELD_HEIGHT//2), (3,FIELD_HEIGHT//2)]
DIRECTIONS = {'left': (-1,0), 'right': (1,0), 'up': (0,-1), 'down': (0,1)}
direction = DIRECTIONS['right']
eaten = False

# apple
apple_pos = place_apple()

while True:
    # clear the field (powershell or terminal)
    os.system('cls') # clear for macos or linux

    # field drawing
    print_field()

    # get input
    txt, _ = timedInput('', timeout=0.3)
    match txt:
        case 'w': direction = DIRECTIONS['up']
        case 'a': direction = DIRECTIONS['left']
        case 's': direction = DIRECTIONS['down']
        case 'd': direction = DIRECTIONS['right']
        case 'q':
            os.system('cls')
            break

    # update the game
    update_snake()
    apple_collision()

    # check death
    if snake_body[0][0] in (0, FIELD_WIDTH - 1) or \
       snake_body[0][1] in (0, FIELD_HEIGHT - 1) or \
       snake_body[0] in snake_body[1:]:
            os.system('cls')
            break