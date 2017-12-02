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
        self.__czyscButon = Button(master, text = 'reset', command=self.czysc)

        self.__label = Label(master, textvariable = self.__tekstLabelki)

        self.__textBox = Text(master, height=10, width=30)
        self.__textBox.insert(END, "MOV AL 0x40\nMOV CL 0x5")

        self.__czyTrybKrokowy = IntVar()
        self.__checkBox= Checkbutton(master, text='CzyTrybKrokowy', variable=self.__czyTrybKrokowy)

        self.__label.pack()
        self.__buton.pack()
        self.__czyscButon.pack()
        self.__okno.pack()
        self.__textBox.pack()
        self.__checkBox.pack(side=LEFT)

        self.__indeksKomendyWTrybieKrokowym = 0

    def __odswiezLablke(self):
        self.__tekstLabelki.set(str(self.__procek))


    def __komendaKlik(self):
        inputData = self.__textBox.get("1.0","end-1c")
        komendy = inputData.split('\n')
        if(self.__czyTrybKrokowy.get() == 0):
            for k in komendy:
                self.__procek.parseAndExecute(k)
        else:
            if(self.__indeksKomendyWTrybieKrokowym < len(komendy)):
                self.__procek.parseAndExecute(komendy[self.__indeksKomendyWTrybieKrokowym])
                self.__indeksKomendyWTrybieKrokowym += 1

        self.__odswiezLablke()

    def czysc(self):
        self.__procek.parseAndExecute('MOV AL 0x0')
        self.__procek.parseAndExecute('MOV AH 0x0')
        self.__procek.parseAndExecute('MOV BL 0x0')
        self.__procek.parseAndExecute('MOV BH 0x0')
        self.__procek.parseAndExecute('MOV CL 0x0')
        self.__procek.parseAndExecute('MOV CH 0x0')
        self.__procek.parseAndExecute('MOV DL 0x0')
        self.__procek.parseAndExecute('MOV DH 0x0')
        self.__textBox.delete('1.0', END)
        self.__indeksKomendyWTrybieKrokowym = 0
        self.__odswiezLablke()

def main():
    ramka = Tk()
    o = Okno(ramka)
    ramka.mainloop()

if __name__ == '__main__':
    main()