class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Lista:
    def __init__(self):
        self.__first = None
        self.__size = 0

    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0

    def __getLastNode(self):
        node = self.__first
        while node.next != self.__first:
            node = node.next

        return node

    def __getPreLastNode(self):
        node = self.__first
        while node.next.next != self.__first:
            node = node.next

        return node

    def add(self, value):
        nowy = Node(value)
        self.__size += 1

        if self.__first is None:
            self.__first = nowy
            nowy.next = self.__first
            return

        ostatni = self.__getLastNode()
        nowy.next = self.__first
        ostatni.next = nowy 
        

    def __assertSize(self, idx):
        if idx >= self.getSize() or idx < 0:
            raise IndexError("Idx {}, size {}".format(idx, self.getSize()))

    def get(self, idx):
        self.__assertSize(idx)
        node = self.__first
        for _ in range(idx):
            node = node.next
        
        return node.value
  
    def clear(self):
        while not self.isEmpty():
            if self.getSize() == 1:
                self.__first.next = None
                self.__first = None
            
            else:    
                preLastNode = self.__getPreLastNode()
                lastNode = preLastNode.next
                preLastNode.next = self.__first
                lastNode = None

            self.__size -= 1