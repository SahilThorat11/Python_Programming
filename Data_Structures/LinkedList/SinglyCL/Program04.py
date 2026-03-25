# DONE
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SinglyCL:

    # DONE
    def __init__(self):
        self.first = None
        self.iCount = 0

    # DONE
    def InsertFirst(self, no):
        newn = Node(no) 

        # LL is empty
        if (self.first == None):
            self.first = newn
            newn.next = self.first
        #LL contains atleast one node
        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            newn.next = self.first
            self.first = newn
            temp.next = self.first

        self.iCount = self.iCount + 1
            
    # DONE
    def InsertLast(self, no):
        newn = Node(no)

        if(self.first == None):
            self.first = newn
            newn.next = self.first

        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            temp.next = newn
            newn.next = self.first

        self.iCount = self.iCount + 1

    # DONE
    def InsertAtPos(self, no, pos):
        
        # Invalid Position
        if((pos < 1) or (pos > self.iCount + 1)):
            print("Invalid Postion")
            return
        
        # If first position
        if(pos == 1):
            self.InsertFirst(no)
        # if last position
        elif(pos == self.iCount + 1):
            self.InsertLast(no)
        # If in between position
        else:
            newn = Node(no)
            temp = self.first

            for i in range(1, pos - 1):
                temp = temp.next

            newn.next = temp.next
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
        if(self.first == None):
            return
        
        temp = self.first

        while True:
            print(f"| {temp.data} | -> ", end="")
            temp = temp.next

            if temp == self.first:
                break

        print()

    # DONE 
    def Count(self):
        return self.iCount

def main():

    sobj = SinglyCL()
    
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    print("Elements of Linked list are : ")
    sobj.Display()

    print("Number of elements in Linked list are : ", sobj.Count())
    print()

    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)

    print("Elements of Linked list are : ")
    sobj.Display()

    print("Number of elements in Linked list are : ", sobj.Count())
    print()

    sobj.InsertAtPos(75, 4)

    print("Elements of Linked list are : ")
    sobj.Display()

    print("Number of elements in Linked list are : ", sobj.Count())
    print()
    
if __name__ == "__main__":
    main()

    