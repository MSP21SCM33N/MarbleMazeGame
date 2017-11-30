#Marble Maze Game

from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

b = (0,0,255)
n = (0,0,0)
g = (0,255,0)
w = (255,255,255)
r = (0, 0, 255)
x = 3
y = 6

board = {}
ballLoc = {}

#Maze 0
ballLoc[0] = (1, 6)
board[0] = [
            [b,b,b,b,b,b,b,b],
            [b,n,n,n,n,n,w,b],
            [b,n,b,b,n,b,b,b],
            [b,n,n,n,n,b,g,b],
            [b,b,n,b,b,b,n,b],
            [b,n,n,b,n,n,n,b],
            [b,n,n,n,n,b,n,b],
            [b,b,b,b,b,b,b,b]
            ]

#Maze 1
ballLoc[1] = (2, 6)
board[1] = [
            [b,b,b,b,b,b,b,b],
            [b,n,n,n,n,n,n,b],
            [b,b,n,b,b,b,w,b],
            [b,n,n,b,n,b,b,b],
            [b,n,n,n,n,b,g,b],
            [b,n,b,b,n,b,n,b],
            [b,n,n,b,n,n,n,b],
            [b,b,b,b,b,b,b,b]
            ]
#Maze 2
ballLoc[2] = (6, 3)
board[2] = [
            [b,b,b,b,b,b,b,b],
            [b,n,n,n,b,n,n,b],
            [b,n,b,b,b,b,n,b],
            [b,n,b,n,n,n,n,b],
            [b,n,n,n,b,b,n,b],
            [b,n,b,b,b,g,n,b],
            [b,n,n,w,b,n,n,b],
            [b,b,b,b,b,b,b,b]
            ]
#Maze 3
ballLoc[3] = (5, 5)
board[3] = [
            [r,r,r,r,r,r,r,r],
            [r,n,n,n,n,r,r,r],
            [r,n,r,r,n,n,r,r],
            [r,n,n,n,n,r,r,r],
            [r,n,r,r,n,n,r,r],
            [r,n,r,r,n,w,r,r],
            [r,n,r,r,n,r,r,r],
            [g,n,r,r,n,r,r,r],
            ]

#Maze 4
ballLoc[4] = (0, 0)
board[4] = [
            [w,n,n,n,b,b,b,b],
            [b,n,b,n,n,n,n,b],
            [b,n,b,n,b,b,n,b],
            [b,n,b,n,n,b,n,b],
            [b,b,b,b,n,b,n,b],
            [b,b,b,b,n,n,n,b],
            [b,n,n,n,n,b,b,b],
            [b,g,b,b,b,b,b,b]
            ]

#Maze 5
ballLoc[5] = (3, 3)
board[5] = [
            [b,n,b,b,b,b,n,b],
            [b,n,n,n,n,n,n,n],
            [b,n,b,b,b,b,n,b],
            [b,n,b,w,n,b,n,b],
            [b,n,b,b,n,b,n,b],
            [n,n,n,n,n,b,n,b],
            [b,b,b,b,b,b,n,b],
            [b,b,b,g,n,n,n,b]
            ]

game = True
playing = True
select = 0

def move_marble(pitch,roll,x,y):
    change_x = x
    change_y = y
    if 10 < pitch < 179 and x != 0:
        change_x -= 1
    elif 181 < pitch < 350 and x != 7:
        change_x += 1
    if 10 < roll < 179 and y != 7:
        change_y += 1
    elif 181 < roll < 350 and y != 0:
        change_y -= 1
    change_x, change_y = check_wall(x,y,change_x,change_y)
    return change_x,change_y

def check_wall(x,y,change_x,change_y):
    if board[select][change_y][change_x] != b:
        return change_x,change_y
    elif board[select][change_y][x] != b:
        return x,change_y
    elif board[select][y][change_x] != b:
        return change_x,y
    else:
        return x,y

while playing:
    select = 0
    sense.show_message("Select maze")
    i = 0
    while i == 0:
        sense.set_pixels(sum(board[select],[]))
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    i = 1
                if event.direction == "right":
                    if select < 5:
                        select += 1
                    else:
                        select = 0
                if event.direction == "left":
                    if select > 0:
                        select -= 1
                    else:
                        select = 5
    x,y = ballLoc[select][1], ballLoc[select][0]

    while game:
        o = sense.get_orientation()
        pitch = o['pitch']
        roll = o['roll']
        x,y = move_marble(pitch,roll,x,y)
        if board[select][y][x] == g:
                game == False
                sense.show_message("You Win!")
                sense.show_message("Press up to play again and down to quit")
        board[select][y][x] = w
        sense.set_pixels(sum(board[select],[]))
        sleep(0.05)
        board[select][y][x] = n 

    i = 0
    while i == 0:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                        i = 1
                        playing = True
                if event.direction == "down":
                        i = 1
                        playing = False