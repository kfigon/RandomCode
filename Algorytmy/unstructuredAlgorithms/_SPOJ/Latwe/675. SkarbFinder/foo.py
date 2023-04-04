__author__ = 'kamil'

class Kierunki:
    polnoc = 0
    poludnie = 1
    zachod = 2
    wschod =3

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def czyStart(self):
        if(self.x == 0 and self.y == 0):
            return True
        else:
            return False

def foo(dane):
    punkt = instrukcjeNaPunkt(dane)

    if(punkt.czyStart()):
        return "studnia"
    else:
        return punktNaInstrukcje(punkt)


def punktNaInstrukcje(punkt):
    instrukcje = []

    if(punkt.y > 0):
        instrukcje.append([Kierunki.polnoc, punkt.y])
    elif(punkt.y < 0):
        instrukcje.append([Kierunki.poludnie, abs(punkt.y)])

    if(punkt.x > 0):
        instrukcje.append([Kierunki.wschod, punkt.y])
    elif(punkt.x < 0):
        instrukcje.append([Kierunki.zachod, abs(punkt.y)])

    return instrukcje

def instrukcjeNaPunkt(zestawInstrukcji):
    punkt = Punkt(0, 0)

    for instr in zestawInstrukcji:
        if(instr[0] == Kierunki.polnoc):
            punkt.y += instr[1]
        elif(instr[0] == Kierunki.poludnie):
            punkt.y -= instr[1]
        elif(instr[0] == Kierunki.wschod):
            punkt.x += instr[1]
        elif(instr[0] == Kierunki.zachod):
            punkt.x -= instr[1]

    return punkt


