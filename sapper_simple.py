import tkinter as tk
from tkinter import messagebox as msg
from functools import partial

from random import shuffle
# shuffle позволяет перемешивать какую-то коллекцию (лист)


# create window with game
window = tk.Tk()
window.title('Saper by tkinter')

#create rows, coluns and buttons
ROW = 7
COLUMN = 7
buttons = []
count_mines = 10
curr_symbol = ''

# получим расположение мин
def get_mines_places():
    count_places = ROW * COLUMN
    a = list(range(1, count_places + 1))
    # print(a)
    shuffle(a)
    # print(a)
    b = a[:count_mines]
    # print(b)
    # b - искомый лист с позициями мин
    return b

mines_places = get_mines_places()
# print(mines_places)
mines_places.sort()
print(mines_places)

game_place = []
for i in range(ROW+2):
    game_place.append(['0'] * (COLUMN+2))
    # print(game_place[i])

count_current_place = 1
count_current_mines = 0
for i in range(1, ROW+1):
    for j in range(1, COLUMN+1):
        if (mines_places[count_current_mines] == count_current_place):
            game_place[i][j] = '*'
            count_current_mines = count_current_mines + 1
            if (count_current_mines == len(mines_places)):
                count_current_mines = 0
        else:
            game_place[i][j] = '1'
        count_current_place = count_current_place + 1

# вывод массива, заполненного минами
# for i in range(ROW+2):
#     for j in range(COLUMN+2):
#         print(game_place[i][j], end=' ')
#     print()

# print()

for i in range(1, ROW+1):
    for j in range(1, COLUMN+1):
        count_mins_near = 0
        if (game_place[i][j] != '*'):
            if(game_place[i - 1][j - 1] == '*'):
                count_mins_near = count_mins_near + 1
            if (game_place[i-1][j] == '*'):
                count_mins_near = count_mins_near + 1
            if (game_place[i-1][j+1] == '*'):
                count_mins_near = count_mins_near + 1
            if (game_place[i][j-1] == '*'):
                count_mins_near = count_mins_near + 1
            if (game_place[i][j+1] == '*'):
                count_mins_near = count_mins_near + 1
            if (game_place[i+1][j - 1] == '*'):
                count_mins_near = count_mins_near + 1
            if (game_place[i+1][j] == '*'):
                count_mins_near = count_mins_near + 1
            if (game_place[i+1][j+1] == '*'):
                count_mins_near = count_mins_near + 1

        if (game_place[i][j] != '*'):
            game_place[i][j] = count_mins_near

# вывод массива, заполненного минами
# for i in range(ROW+2):
#     for j in range(COLUMN+2):
#         print(game_place[i][j], end=' ')
#     print()



# создание двумерного списка с кнопками
for i in range(ROW):
    temp = []
    for j in range(COLUMN):
        btn = tk.Button(window, width=3, font='Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)


# def restart_table(position, curr_symbol):



def click_button(curr_i, curr_j):
    print(curr_i + 1, curr_j + 1)
    curr_symbol = game_place[curr_i + 1][curr_j + 1]
    position = (curr_i + 1) * ROW + (curr_j + 1)
    print("position =", position)
    if(curr_symbol == '*'):
        btn[position].config(text=curr_symbol)
        msg.showinfo('GAME OVER!', 'It was a bomb!')
    else:
        print(curr_symbol)



for i in range(ROW):
    for j in range(COLUMN):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)
        # position = i + j
        btn.config(command=partial(click_button, i, j))
        # btn[position].config(text=curr_symbol)
        # btn.config(command=lambda button=btn: click_button(button))
        # print(res_position, res_symbol)
window.mainloop()
