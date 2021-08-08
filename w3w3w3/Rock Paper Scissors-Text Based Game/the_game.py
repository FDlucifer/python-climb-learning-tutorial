'''imports'''
import time
import sys
import random


def win():
    print('THE GAME: You win.')

def lost():
    print('THE GAME: You lost.')

def draw():
    print('THE GAME: Its a draw.')


def the_game():

    moves = ['rock', 'paper', 'scissors']

    print('THE GAME: Rock, Paper, Scissors?')
    attempts = 3
    while True:
        if attempts == 0:
            print('THE GAME: You failed to provide a correct option to play the game. Goodbye.')
            time.sleep(3)
            sys.exit(0)

        player = str(input('Player: ')).lower()
        if player.lower() not in moves:
            print(f'THE GAME: Invalid Option! You have {attempts} attempts left.')
            attempts -= 1
        else:
            computer = random.choice(moves)
            print(f'Computer: {computer}')

            if player == computer:
                draw()
            elif player == 'rock' and computer == 'scissors':
                win()
            elif player == 'rock' and computer == 'paper':
                lost()
            elif player == 'paper' and computer == 'rock':
                win()
            elif player == 'paper' and computer == 'scissors':
                lost()
            elif player == 'scissors' and computer == 'paper':
                win()
            elif player == 'scissors' and computer == 'rock':
                lost()
            else:
                pass

            play_again = str(input('THE GAME: Retry? (y/n): '))
            if play_again.lower() == 'y':
                the_game()
            elif play_again.lower() == 'n':
                print('THE GAME: Game Over. Goodbye.')
                time.sleep(2.5)
                sys.exit(0)
            else:
                print('THE GAME: Invalid Options. Goodbye.')
                time.sleep(2.5)
                sys.exit(0)


if __name__=='__main__':
    the_game()
