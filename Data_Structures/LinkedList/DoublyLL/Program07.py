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

    # DONE
    def InsertFirst(self, no):
        newn = Node(no)

        # if LL is empty
        if(self.first == None):
            self.first = newn
        #if LL contains at least one node
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.iCount = self.iCount + 1
    
    # DONE
    def InsertLast(self, no):
        newn = Node(no)

        # If LL is Empty
        if(self.first == None):
            self.first = newn;
        #if LL contains at least one node
        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next
            
            temp.next = newn
            newn.prev = temp

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

            for i in range(1, pos - 1):
                temp = temp.next

            newn.next = temp.next
            temp.next.prev = newn
            temp.next = newn
            newn.prev = temp

            self.iCount = self.iCount + 1

    # DONE
    def DeleteFirst(self):
        
        # If LL is empty
        if(self.first == None):
            return
        # if LL contains single node
        elif(self.first.next == None):
            self.first = None
        # if LL contains more than one node
        else:
            self.first = self.first.next
            self.first.prev = None
        
        self.iCount = self.iCount - 1

    # DONE
    def DeleteLast(self):
        # If LL is empty
        if(self.first == None):
            return
        # if LL contains single node
        elif(self.first.next == None):
            self.first = None
        # if LL contains more than one node
        else:
            temp = self.first

            while(temp.next.next != None):
                temp = temp.next
            
            temp.next = None
        
        self.iCount = self.iCount - 1
    
    def DeleteAtPos(self, pos):
        pass
    
    # DONE
    def Display(self):
        temp = None

        temp = self.first

        print("None <=> ", end = " ")

        while(temp != None):
            print("|", temp.data, "| <=> ", end = "")
            temp = temp.next

        print(None)

    # DONE 
    def Count(self):
        return self.iCount

def main():

    dobj = DoublyLL()

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

    dobj.DeleteFirst()

    print("Elements of Linked list are : ")
    dobj.Display()
    print("Number of elements in Linked list are : ", dobj.Count())
    print()

    dobj.DeleteLast()

    print("Elements of Linked list are : ")
    dobj.Display()
    print("Number of elements in Linked list are : ", dobj.Count())
    print()

    
if __name__ == "__main__":
    main()

    