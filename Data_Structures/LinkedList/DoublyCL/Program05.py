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
    
    # DONE
    def InsertLast(self, no):
        newn = Node(no)

        # if LL is empty
        if (self.first == None) and (self.last == None):
            self.first = newn
            self.last = newn
        # If LL is conatins atleast one node
        else:
            self.last.next = newn
            newn.prev = self.last
            self.last = newn

        self.first.prev = self.last
        self.last.next = self.first

        self.iCount = self.iCount + 1

    # DONE
    def InsertAtPos(self, no, pos):
        # Invalid Position
        if((pos < 1) or (pos > self.iCount + 1)):
            print("Invalid Position")
            return

        # first position
        if(pos == 1):
            self.InsertFirst(no)
        # last position
        elif(pos == self.iCount + 1):
            self.InsertLast(no)
        # Inbetween position
        else:
            newn = Node(no)
            temp = self.first

            for _ in range(1, pos - 1):
                temp = temp.next

            newn.next = temp.next
            temp.next.prev = newn
            newn.prev = temp
            temp.next = newn

            self.iCount = self.iCount + 1


    def DeleteFirst(self):
        pass

    def DeleteLast(self):
        pass
    
    def DeleteAtPos(self, pos):
        pass
    
    # DONE
    def Display(self):
        # if LL is empty
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

    dobj.InsertLast(101)
    dobj.InsertLast(111)
    dobj.InsertLast(121)

    print("Elements of Linked list are : ")
    dobj.Display()
    print("Number of elements in Linked list are : ", dobj.Count())
    print()
    
    dobj.InsertAtPos(75, 4)

    print("Elements of Linked list are : ")
    dobj.Display()
    print("Number of elements in Linked list are : ", dobj.Count())
    print()
    
if __name__ == "__main__":
    main()

    