# DONE
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyCL:

    # DONE
    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0

    # DONE
    def InsertFirst(self, no):
        newn = Node(no)

        # if LL is empty
        if((self.first == None) and (self.last == None)):
            self.first = newn
            self.last = newn
        # If LL is conatins atleast one node
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.first.prev = self.last
        self.last.next = self.first

        self.iCount = self.iCount + 1
    
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
    
    # DONE
    def Display(self):
        if((self.first == None) and (self.last == None)):
            print("Linked list is Empty")
            return

        temp = self.first

        print("<=> ", end="")

        while True:
            print("|", temp.data, "| <=> ", end = "")
            temp = temp.next
            if(temp == self.first):
                break

        print()

    # DONE 
    def Count(self):
        return self.iCount

def main():

    dobj = DoublyCL()

    dobj.InsertFirst(51)
    dobj.InsertFirst(21)
    dobj.InsertFirst(11)

    print("Elements of Linked list are : ")
    dobj.Display()
    print("Number of elements in Linked list are : ", dobj.Count())
    print()
    
if __name__ == "__main__":
    main()

    