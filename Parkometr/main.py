__author__ = 'kamil'

from ModelKonsolowy import ModelKonsolowyParkometru

def main():
    p = ModelKonsolowyParkometru()

    wejscie = '1'

    while(wejscie != "exit"):
        print("\n")
        print("parkomat")
        print("+ -> zwieksza minuty")
        print("- -> zmniejsza minuty")
        print("++ -> zwieksza o godizne")
        print("-- -> zmmniejsza o godzine")
        print("licz - liczy kwote")
        print("exit - koniec")

        p.piszCeneZaGodizne()
        p.piszWybranyCzas()
        wejscie = input(">")

        if (wejscie == "+"):    p.zwiekszMinuty()
        elif(wejscie == "-"):   p.zmniejszMinuty()
        elif(wejscie == "++"):  p.zwiekszGodzine()
        elif(wejscie == "--"): p.zmniejszGodzine()
        elif(wejscie == "licz"):
            p.piszKwote()

        else:
            print("niepoprawna komenda")

if __name__ == "__main__":
    main()