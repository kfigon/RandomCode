__author__ = 'kamil'

class Node:
    def __init__(self, key):
        self.__lewy = None
        self.__prawy = None
        self.__key = key

    def getLewy(self):
        return self.__lewy
    def setLewy(self, node):
        self.__lewy = node

    def getPrawy(self):
        return self.__prawy
    def setPrawy(self, node):
        self.__prawy = node

    def getKey(self):
        return self.__key


class BST:
    def __init__(self):
        self.__root = None

    # rekurencyjny algorytm
    def inOrder(self):
        list = []
        self.__inOrderInternal(self.__root, list)
        return list

    def __inOrderInternal(self, node, outputList):
        if(node != None):
            self.__inOrderInternal(node.getLewy(), outputList)
            outputList.append(node.getKey())
            self.__inOrderInternal(node.getPrawy(), outputList)

    def dodaj(self, key):
        nowy = Node(key)
        if(self.__root == None):
            self.__root = nowy
            return

        wsk = self.__root
        poprzedzajacyWsk = None
        while(wsk != None):
            poprzedzajacyWsk = wsk
            if(nowy.getKey() <= wsk.getKey()):
                wsk = wsk.getLewy()
            else:
                wsk = wsk.getPrawy()

        wsk = nowy
        if(nowy.getKey() <= poprzedzajacyWsk.getKey()):
            poprzedzajacyWsk.setLewy(nowy)
        else:
            poprzedzajacyWsk.setPrawy(nowy)

    # zwraca wezel
    def search(self, key):
        return self.__searchInternal(self.__root, key)

    def __searchInternal(self, node, key):
        if(node == None or node.getKey() == key):
            return node
        if(key <= node.getKey()):
            return self.__searchInternal(node.getLewy(), key)
        else:
            return self.__searchInternal(node.getPrawy(), key)

    def searchIterative(self, key):
        node = self.__root
        while(node != None and node.getKey() != key):
            if(key <= node.getKey()):
                node = node.getLewy()
            else:
                node = node.getPrawy()

        return node

    def isEmpty(self):
        return (self.__root == None)

    # zwraca wartosc!
    def getMin(self):
        if(self.isEmpty()):
            return None

        wsk = self.__root
        val = wsk.getKey()
        while(wsk!=None):
            val = wsk.getKey()
            wsk = wsk.getLewy()
        return val

    def getMax(self):
        if(self.isEmpty()):
            return None

        wsk = self.__root
        val = wsk.getKey()
        while(wsk!=None):
            val = wsk.getKey()
            wsk = wsk.getPrawy()
        return val