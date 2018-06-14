import argparse
# -h z automatu

parser = argparse.ArgumentParser(description="moj program!")
parser.add_argument("mojArg", help="podaj liczbe", type=int) # wymagany, pozycyjny. kolejnosc dowolna
# foo.py -v 5

#  tylko flaga. '-' wiec opcjonalny
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

parser.add_argument('-b', action="store")
parser.add_argument('-c', action="store", type=int, default=55)

args = parser.parse_args()
print("liczba: " + str(args.mojArg))
print("verbose: " + str(args.verbose))
print("b: " + str(args.b))
print("c: " + str(args.c))


# python foo.py -v -b asd -c 123 5
# python foo.py -v -b asd -c 123 <- blad! brak mojArg
# python foo.py 5 -v -b asd -c 123 to samo wyzej