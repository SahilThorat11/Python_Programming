# DONE
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:

    # DONE
    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self, no):
        pass
    
    def InsertLast(self, no):
        pass

    def InsertAtPos(self, no, pos):
        pass

    def DeleteFirst(self):
        pass

    def DeleteLast(self):
        pass
    
    def DeleteAtPos(self, pos):
        pass
    
    def Display(self):
        pass

    # DONE 
    def Count(self):
        return self.iCount

def main():

    dobj = DoublyLL()

    print("Number of elements in Linked list are : ", dobj.Count())
    
if __name__ == "__main__":
    main()

    