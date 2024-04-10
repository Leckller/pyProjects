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
        return frame

    def button(self, frame: frame, w: int, h: int, t: str, x: int, y: int):
        button = tk.Button(frame, width=w, height=h, text=t)
        button.place(x=x, y=y)
        return button

    def start(self):
        visor = self.frame(300, 50, "#fcb900", 0, 0)
        body = self.frame(300, 350, "#4f3b02", 1, 0)

        clear_button = self.button(body, 19, 2, "C", 0, 0)
        resto_button = self.button(body, 4, 2, "%", 180, 0)
        div_button = self.button(body, 4, 2, "/", 240, 0)

        self.window.mainloop()


calculadora = Calculadora()

calculadora.start()
