import tkinter as tk


class Calculadora:
    window = tk.Tk()

    def __init__(self):
        self.window.geometry("300x400")
        self.window.title("Calculadora")

    def frame(
        self,
        width: int,
        height: int,
        color: str = "#000000",
        n_row: int = 0,
        n_column: int = 0,
    ):
        frame = tk.Frame(self.window, width=width, height=height, bg=color)
        frame.grid(row=n_row, column=n_column)

    def start(self):
        self.frame(300, 50, "#fcb900", 0, 0)
        self.frame(300, 350, "#4f3b02", 1, 0)

        self.window.mainloop()


calculadora = Calculadora()

calculadora.start()
