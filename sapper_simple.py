import tkinter as tk
from tkinter import messagebox as msg

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


# создание двумерного списка с кнопками
for i in range(ROW):
    temp = []
    for j in range(COLUMN):
        current_i = i
        current_j = j
        btn = tk.Button(window, width = 3, font='Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)

def click_button(clicked_button):
    print(clicked_button)
    clicked_button.config(state='disabled')
    # print(repr(clicked_button))

    # -------------------------------   вариант 1 ---------------------------#
    current_click_position_check = 1
    #click_position надо считать, это чисто примерн
    click_position = 13
    for i in range(1, ROW + 1):
        for j in range(1, COLUMN+1):
            if (click_position == current_click_position_check):
                if game_place[i][j] == '*':
                    clicked_button.config(text='*')
                    msg.showinfo(title="End Game", message="It was a bomb!")
                    window.destroy()
                else:
                    button_text = game_place[i][j]
                    print(button_text)
                    clicked_button.config(text=button_text)
            else:
                current_click_position_check = current_click_position_check + 1




# вывод кнопок на экран
for i in range(ROW):
    for j in range(COLUMN):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)
        # btn = tk.Button(window, text='c', command=lambda j=c: click_button(j))
        btn.config(command=lambda button=btn: click_button(button))

window.mainloop()
