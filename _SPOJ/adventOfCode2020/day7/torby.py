from typing import List, Tuple, Dict, Set
import re


# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; 
# bags must be color-coded and must contain specific quantities of other color-coded bags. 
# Apparently, nobody responsible for these regulations considered how long they would take to enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# These rules specify the required contents for 9 bag types. 

# In this example, every faded blue bag is empty, every vibrant plum 
# bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least 
# one other bag, how many different bag colors would be valid for the outermost bag? 
# (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

# In the above rules, the following options would be available to you:

# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag? 
# (The list of rules is quite long; make sure you get all of it.)

def parseLine(line: str) -> Tuple[str, Dict[str, int]]:
    rules = line.split('contain')
    bagRule = rules[0].replace('bags','').strip()
    if 'no other bags' in rules[1]: 
        return bagRule, {}

    containedBags = rules[1].split(',')
    d: Dict[str, int] = {}
    for bag in containedBags:
        cleanedString = bag.replace('bags', '').replace('bag','').replace('.','').strip()
        result = re.findall(r'(\d+) (\w+ \w+)', cleanedString)

        if result:
            assert len(result) == 1
            d[result[0][1]] = int(result[0][0])
    
    return bagRule, d

def parseData(content: str) -> Dict[str, Dict[str, int]]:
    d: Dict[str, Dict[str, int]] = {}
    rules = content.splitlines()
    for rule in rules:
        parsed = parseLine(rule)
        d[parsed[0]] = parsed[1]
    return d

def findWhereBagIsLocated(rules: Dict[str, Dict[str, int]], bagColorToFind: str) -> int:
    cnt: int = 0

    visited: Set[str] = set()

    def traverse(node: str, toFind: str):
        bags = rules[node]
        if toFind not in bags or node in visited or len(bags) == 0:
            return
        
        visited.add(node)
        nonlocal cnt
        cnt += 1

        for r in rules:
            traverse(r, node)

    for r in rules:
        traverse(r, bagColorToFind)

    print(cnt)
    return cnt
        

inputData = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

rules = inputData.splitlines()
parsedRules = list(map(parseLine, rules))

assert parsedRules[0] == ('light red', {'bright white': 1, 'muted yellow':2})
assert parsedRules[2] == ('bright white', {'shiny gold': 1})
assert parsedRules[7] == ('faded blue', {})
assert parseLine('shiny green bags contain 2 bright lavender bags, 3 shiny olive bags, 4 mirrored violet bags, 5 posh white bags.') == ('shiny green', {'bright lavender': 2, 'shiny olive': 3, 'mirrored violet':4, 'posh white':5})

assert findWhereBagIsLocated(parseData(inputData), 'shiny gold') == 4
assert findWhereBagIsLocated(parseData(inputData), 'light red') == 0

with open('inputData.txt') as f:
    assert findWhereBagIsLocated(parseData(f.read()), 'shiny gold') == 124