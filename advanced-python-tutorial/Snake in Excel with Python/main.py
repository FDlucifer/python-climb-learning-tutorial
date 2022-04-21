from random import randint
import xlwings as xw
from string import ascii_uppercase
from time import sleep
from sys import exit

class Snake:
    def __init__(self, speed, width, height):

        # book setup
        self.book = xw.Book()
        self.sheet = self.book.sheets[0]
        self.sheet.name = 'snake'

        # board setup
        self.speed = 1/speed
        self.width = width
        self.height = height
        self.board_setup()

        # snake setup
        self.body = [(int(height / 2), 5), (int(height / 2), 4), (int(height / 2), 3)]
        self.direction = (0,1)
        self.eaten = False
        self.create_apple()

    def board_setup(self):

        # background color
        game_cells = f'B2:{ascii_uppercase[self.width]}{self.height + 1}'
        self.sheet[game_cells].color = board_color

        control_cells = f'B{self.height + 2}:{ascii_uppercase[self.width]}{self.height + 6}'
        self.sheet[control_cells].color = control_color

        # buttons
        self.exit_cell = f'{ascii_uppercase[self.width]}{self.height + 6}'
        self.sheet[self.exit_cell].value = 'quit'

        self.left_cell = f'C{self.height + 4}'
        self.sheet[self.left_cell].value = 'left'

        self.right_cell = f'E{self.height + 4}'
        self.sheet[self.right_cell].value = 'right'

        self.up_cell = f'D{self.height + 3}'
        self.sheet[self.up_cell].value = 'up'

        self.down_cell = f'D{self.height + 5}'
        self.sheet[self.down_cell].value = 'down'

        # button styling
        for button in [self.exit_cell, self.left_cell, self.right_cell, self.up_cell, self.down_cell]:
            self.sheet[button].color = button_color
            self.sheet[button].font.color = text_color

        # cell dimensions
        self.sheet[f'B2:B{self.height + 6}'].row_height = 40

    def display_game_elements(self):
        # apple display
        self.sheet[self.apple_pos].color = apple_color

        # snake body
        for index, cell in enumerate(self.body):
            if index == 0:
                self.sheet[cell].color = head_color
            else:
                self.sheet[cell].color = body_color

    def create_apple(self):
        # get a random cell (row,col)
        row = randint(1,self.height)
        col = randint(1,self.width)

        # check if apple is below snake
        while (row, col) in self.body:
            row = randint(1,self.height)
            col = randint(1,self.width)

        self.apple_pos = (row, col)

    def input(self):
        selected_cell = self.book.selection.address.replace('$', '')
        if selected_cell == self.right_cell:
            self.direction = (0,1)
        elif selected_cell == self.left_cell:
            self.direction = (0,-1)
        elif selected_cell == self.up_cell:
            self.direction = (-1,0)
        elif selected_cell == self.down_cell:
            self.direction = (1,0)

    def exit_game(self):
        selected_cell = self.book.selection.address.replace('$', '')
        if selected_cell == self.exit_cell:
            self.book.close()
            exit()

    def move_snake(self):
        if self.eaten:
            new_body = self.body[:]
            self.eaten = False
        else:
            lost_cell = self.body[-1]
            new_body = self.body[:-1]
            self.sheet[lost_cell].color = board_color

        new_head = self.add_direction(new_body[0], self.direction)
        new_body.insert(0,new_head)

        self.body = new_body

    def add_direction(self, cell, direction):
        row = cell[0] + direction[0]
        col = cell[1] + direction[1]
        return(row, col)

    def check_apple_collision(self):
        if self.body[0] == self.apple_pos:
            self.eaten = True
            self.create_apple()

    def check_fail(self):
        head = self.body[0]
        body = self.body[1:]

        if head in body or head[1] <= 0 or head[1] >= self.width+1 or head[0] <= 0 or head[0] >= self.height+1:
            self.book.close()
            exit()

    def run(self):
        while True:
            self.exit_game()
            sleep(self.speed)
            self.input()
            self.move_snake()
            self.check_apple_collision()
            self.check_fail()
            self.display_game_elements()

# colors
board_color = (226,227,223)
control_color = (46,50,51)
button_color = (81,91,94)
text_color = (255,255,255)
apple_color = (0,255,100)
head_color = (255,0,0)
body_color = (200,0,0)

snake = Snake(3,12,8)
snake.run()