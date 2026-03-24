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
    
    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    print("Elements of Linked list are : ")
    sobj.Display()

    print("Number of elements in Linked list are : ", sobj.Count())
    print()

    
if __name__ == "__main__":
    main()

    