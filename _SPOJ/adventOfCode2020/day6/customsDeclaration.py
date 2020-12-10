from typing import List, Dict

# you filled customs declaration form:
# 26 yes/no questions marked a-z. Answers "yes" are written, rest are "no"

# people fill that in groups and e.g. in one:
# abcx
# abcy
# abcz

# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. 
# (Duplicate answers to the same question don't count extra; each question counts at most once.)

# Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b

# This list represents answers from five groups:

# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.
# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

# ---------------------------------------------
# v2
# you notice that you misread one word in the instructions
# You don't need to identify the questions to which anyone answered "yes"; 
# you need to identify the questions to which everyone answered "yes"!

# This list represents answers from five groups:

# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

inputData = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

def parseData(content: str) -> List[str]:
    groups: List[str] = content.split('\n\n')
    answers: List[str] = []

    for group in groups:
        lines = group.splitlines()
        groupAsnwer = ''
        for line in lines:
            for c in line:
                groupAsnwer += c
        answers.append(groupAsnwer)
    return answers

def countAnswers(answersInGroup: str) -> int:
    d: Dict[str, int] = {}
    for answer in answersInGroup:
        if answer in d:
            d[answer] += 1
        else:
            d[answer] = 1

    return len(d)

def sumAnswers(answersInGroups: List[str]) -> int:
    return sum(map(countAnswers, answersInGroups))

assert parseData(inputData) == ['abc','abc','abac','aaaa','b']
assert sumAnswers(parseData(inputData)) == 11

with open('inputData.txt') as f:
    parsedAnswers = parseData(f.read())
    answerNum = sumAnswers(parsedAnswers)
    assert answerNum == 6335