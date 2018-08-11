class Foo:
    @staticmethod
    def metodaStatyczna(x):
        print("static! " + str(x))

    @classmethod
    def metodaKlasy(cls, x):
        print("metoda zawolana z klasy {} z argumentem {}"
        .format(str(cls), str(x)))


f = Foo()
Foo.metodaStatyczna(123)
Foo.metodaKlasy(123)