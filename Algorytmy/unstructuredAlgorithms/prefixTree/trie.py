from typing import Dict, List, Optional

class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word: str):
        currentNode: Node = self.root

        for i,c in enumerate(word):
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                newNode = Node()
                currentNode.children[c] = newNode
                currentNode = newNode
            if i == len(word)-1:
                currentNode.isWord = True

    def find(self, prefix: str) -> List[str]:
        prefixNode = self.root
        for c in prefix:
            if c not in prefixNode.children:
                return []
            prefixNode = prefixNode.children[c]
        
        return self.traverse(prefix, prefixNode, [])
    
    def traverse(self, prefix: str, node: Optional[Node], out: List[str]) -> List[str]:
        if not node:
            return out
        if node.isWord:
            out.append(prefix)
        for c in node.children:
            nextNode = node.children[c]
            self.traverse(prefix+c, nextNode, out)
        return out

t = Trie()
words = ['app','apple','ape','hi','hello','hell','howdy']
for w in words:
    t.add(w)

def printx(s: str):
    print(f'\"{s}\" -> {t.find(s)}')


printx('')

printx('a')
printx('ap')
printx('app')
printx('appl')
printx('apple')

printx('h')
printx('hell')
printx('hello')
printx('ho')
printx(' ')
printx('asd')