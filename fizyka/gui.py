from tkinter import *
class Movehandler:
    def do(self):
        pass
        
class Okno:
    WIDTH = 300
    HEIGHT = 250
    
    def __init__(self, timeTick=200):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=self.WIDTH, height=self.HEIGHT, bg="white")
        self.canvas.pack()
        self.timeTick = timeTick # milisekundy

    # move handler - obiekt z metoda 'do()' 
    def start(self, moveHandler):
        self.__akcjaRuchowa = moveHandler
        self.__update()
        self.tk.mainloop()
        
    def __update(self):
        self.__akcjaRuchowa.do()
        self.tk.after(self.timeTick, self.__update)


if __name__ == "__main__":

    
    o = Okno()
    # sztuczka z lokalizacja, moze sie przyda w przyszlosci
    o.tk.bind('<Motion>',lambda event: print("{}, {}".format(event.x, event.y)))

    class ruch(Movehandler):
        def do(self):
            print('hi')

    o.start(ruch())
