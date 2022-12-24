import tkinter as tk

# create window with game
window = tk.Tk()

#create rows, coluns and buttons
ROW = 5
COLUMN = 5
buttons = []
count_mines = 15
mines = [ROW][COLUMN]

for i in range(ROW):
    temp = []
    for j in range(COLUMN):
        btn = tk.Button(window, width = 3, font='Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)

for i in range(ROW):
    for j in range(COLUMN):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)

window.mainloop()