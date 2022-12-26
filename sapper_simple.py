import tkinter as tk

from random import shuffle
# shuffle позволяет перемешивать какую-то коллекцию (лист)



# create window with game
window = tk.Tk()

#create rows, coluns and buttons
ROW = 4
COLUMN = 4
buttons = []
count_mines = 3
MINES = 3

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


current_i = 0
current_j = 0

def click_button(clicked_button):
    print(clicked_button)



# создание двумерного списка с кнопками
for i in range(ROW):
    temp = []
    for j in range(COLUMN):
        current_i = i
        current_j = j
        btn = tk.Button(window, width = 3, font='Calibri 15 bold')
        btn.config(command=lambda button=btn: click_button(button))
        temp.append(btn)
    buttons.append(temp)


# вывод кнопок на экран
for i in range(ROW):
    for j in range(COLUMN):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)
        # btn.bind('<Button-1>', click_button)

window.mainloop()
