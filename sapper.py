import tkinter as tk


class MineSweeper:
    # создание стартого окна
    window = tk.Tk()

    # создание таблицы поля
    ROW  = 5
    COLUMNS = 5

    # Метод, который автоматически запускается при вызове всего класса
    # Данный метод необходим для инициализации игры (создание всех данных, которые в дальнейшем будем обрабатывать)
    def __init__(self):
        # двумерный список всех кнопок
        self.buttons = []

        # каждая ячейка таблицы - кнопка, на которую можно нажать
        # моздание кнопок
        for i in range(MineSweeper.ROW):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                btn = tk.Button(MineSweeper.window, width=3, font='Calibri 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        # вывод всех кнопок на экране window
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.print_buttons()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        # вывод всех кнопок в консоли
        for row_btn in self.buttons:
            print(row_btn)


game = MineSweeper()
game.start()

