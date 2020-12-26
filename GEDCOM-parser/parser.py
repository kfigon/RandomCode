from typing import List, Tuple
import re

class GedcomModel:
    source: str
    fullSource: str
    fileVersion: str

    fileDate: str

    version: str
    encoding: str

def extractLine(line: str) -> Tuple[int, str, str]:
    elements = re.match('(\d+) (\w+)(.*)', line)
    if not elements:
        raise Exception(f'invalid line structure {line}')
    parsed = elements.groups()
    rest = parsed[2] if len(parsed) > 2 else ''

    return int(parsed[0]), parsed[1], rest

def parse(content:str) -> GedcomModel:
    lines: List[str] = content.splitlines()
    if len(lines) == 0:
        raise Exception(f'invalid file, no lines')

    model = GedcomModel()
    previousIndentation = -1
    parentTag = ''

    # add tree-like structure in parsing

    for line in lines:
        indentation, tag, content = extractLine(line)

        if previousIndentation == indentation-1:
            parentTag = tag


        previousIndentation = indentation

    return model

