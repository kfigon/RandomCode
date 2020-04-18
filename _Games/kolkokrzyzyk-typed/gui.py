import tkinter as tk

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.plotno = tk.Canvas(self.root, width=300, height=300)
        tk.Button(self.root, text='czysc', command=lambda: self.plotno.delete('all')).pack()

    def draw(self) -> None:
        self.plotno.create_oval(10,20, 40, 40, fill='blue')
        self.plotno.create_line(0, 40, 300, 340, width=2, fill='black')

    def start(self) -> None:
        self.plotno.pack()
        self.root.mainloop()

g = Gui()
g.draw()
g.start()