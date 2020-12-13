from tkinter import *
import random

WIDTH = 300
HEIGHT = 250
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(0, 0, 25, 25, fill='black')
        self.vx = 10
        self.vy = 10

    def update(self):
        canvas.move(self.shape, self.vx, self.vy)
        
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.vx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.vy *= -1

    def move(self):
        self.update()
        tk.after(50, self.move) # 50ms

ball = Ball()
ball.move()

# sztuczka z lokalizacja, moze sie przyda w przyszlosci
tk.bind('<Motion>',lambda event: print("{}, {}".format(event.x, event.y)))

tk.mainloop()

