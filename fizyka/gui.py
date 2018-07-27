from tkinter import *

class Okno:
    WIDTH = 300
    HEIGHT = 250
    
    def __init__(self, akcjaRuchowa):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=self.WIDTH, height=self.HEIGHT, bg="white")
        self.canvas.pack()
        self.__akcjaRuchowa = akcjaRuchowa

    def start(self):
        self.__update()
        self.tk.mainloop()
        
    def __update(self):
        self.__akcjaRuchowa()
        self.tk.after(50, self.__update) # 50ms


if __name__ == "__main__":

    o = Okno(lambda: print("hi"))
    o.start()
