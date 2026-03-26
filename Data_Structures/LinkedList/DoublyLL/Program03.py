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
        temp = None

        temp = self.first

        print("None <=> ", end = " ")

        while(temp != None):
            print("| ", temp.data, " | <=> ", end = " ")
            temp = temp.next

        print(None)

    # DONE 
    def Count(self):
        return self.iCount

def main():

    dobj = DoublyLL()

    dobj.InsertFirst(101)
    dobj.InsertFirst(51)
    dobj.InsertFirst(21)
    dobj.InsertFirst(11)

    print("Elements of Linked list are : ")
    dobj.Display()
    print("Number of elements in Linked list are : ", dobj.Count())
    print()

    
if __name__ == "__main__":
    main()

    