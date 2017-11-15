__author__ = 'kamil'
from tkinter import *
from SymulatorProcesora.Procesor import *
class Okno:
    def __init__(self, master):
        self.__procek = Procesor()
        self.__tekstLabelki = StringVar()
        self.__odswiezLablke()

        self.__okno = Canvas(master, width=300, height=100)
        self.__buton = Button(master, text = 'odpal komende', command=self.__komendaKlik)
        self.__label = Label(master, textvariable = self.__tekstLabelki)

        self.__textBox = Text(master, height=10, width=30)
        self.__textBox .insert(END, "MOV AL 0x40")

        self.__label.pack()
        self.__buton.pack()
        self.__okno.pack()
        self.__textBox .pack()

    def __odswiezLablke(self):
        self.__tekstLabelki.set(str(self.__procek))

    def __komendaKlik(self):
        inputData = self.__textBox.get("1.0","end-1c")
        komendy = inputData.split('\n')
        for k in komendy:
            self.__procek.parseCommand(k)
        self.__odswiezLablke()

def main():
    ramka = Tk()
    o = Okno(ramka)
    ramka.mainloop()

if __name__ == '__main__':
    main()