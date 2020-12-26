def validIban(code: str) -> bool:
    rearranged = (code[4:] + code[:4]).replace(' ','').strip()
    converted = ''
    for c in rearranged:
        converted += convert(c)
    return int(converted) % 97 == 1

def convert(char: str) -> str:
    if len(char) != 1:
        raise Exception(f'invalid char to convert {char}, should be one char')

    if char.isdigit():
        return char
    return str(ord(char) - 55)

assert convert('A') == '10'
assert convert('B') == '11'
assert convert('Z') == '35'

assert validIban('GB82 WEST 1234 5698 7654 32') == True
assert validIban('gb82 WEST 1234 5698 7654 32') == False
assert validIban('GB82 WEST 1234 5698 7654 22') == False
assert validIban('GB82 WEST 1234 6698 7654 32') == False
assert validIban('GB82WEST12345698765432') == True

assert validIban('BE71 0961 2345 6769') == True
assert validIban('BE71 0962 2345 6769') == False
assert validIban('BR15 0000 0000 0000 1093 2840 814 P2') == True
assert validIban('BR15 0002 0000 0000 1093 2840 814 P2') == False
assert validIban('FR76 3000 6000 0112 3456 7890 189') == True
assert validIban('FR76 3000 6000 0112 34A6 7890 189') == False
assert validIban('MU43 BOMM 0101 1234 5678 9101 000 MUR') == True
assert validIban('MU43 BOMM 0101 123G 5678 9101 000 MUR') == False
assert validIban('PL10 1050 0099 7603 1234 5678 9123') == True

print('gut')