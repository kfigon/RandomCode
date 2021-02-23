# https://www.hackerrank.com/challenges/counting-valleys/problem

def countValleys(stepsRecord: str) -> int:
    valeys = 0
    currentHeight = 0
    for s in stepsRecord:
        prevHeight = currentHeight
        if s == 'U':
            currentHeight += 1
        elif s =='D':
            currentHeight -= 1

        if prevHeight < 0 and currentHeight == 0:
            valeys +=1

    return valeys

assert countValleys('UDDDUDUU') == 1
assert countValleys('UDDDUDUDUU') == 1
assert 6 == countValleys('UDUDDUUUDUDUDUUDUUDDDDDUDUDDDDUUDDUDDUUUUDUUDUDDDDUDUDUUUDDDUUUDUDDUUDDDUUDDUDDDUDUUDUUDUUDUDDDUUUUU')
print('oka')