__author__ = 'kamil'

class Node:
    item = None
    next = None

class Stos:
    def __init__(self):
        self.__size = 0
        self.__top = Node()

    def isEmpty(self):
        return (self.__size == 0)

    def getSize(self):
        return self.__size

    def push(self, item):
        toAdd = Node()
        toAdd.item = item
        toAdd.next = self.__top
        self.__top = toAdd
        self.__size += 1

    def pop(self):
        if(self.isEmpty()):
            return None

        toRet = self.__top.item
        self.__top = self.__top.next
        self.__size -= 1
        return toRet

    def clean(self):
        while(not self.isEmpty()):
            self.pop()
