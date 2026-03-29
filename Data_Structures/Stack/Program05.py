
class Node:
    def __init__(self, no):
        self.data = no
        self.next = None


class Stack:
    
    def __init__(self):
        print("Stack gets created successfully...")
        self.first = None
        self.iCount = 0

    def Push(self, no):
        newn = Node(no)

        newn.next = self.first
        self.first = newn

        self.iCount = self.iCount + 1

    def Pop(self):
        if self.first is None:
            print("Stack is empty")
            return None   

        value = self.first.data
        temp = self.first

        self.first = self.first.next
        del temp

        self.iCount = self.iCount - 1
        return value

    def peep(self):
        pass

    def Display(self):
        temp = self.first

        if(self.first is None):
            print("Stack is empty")
            return
        
        while temp is not None:
            print("|", temp.data, "|")
            temp = temp.next

    def Count(self):
        return self.iCount        

def main():
    sobj = Stack()
    
    sobj.Push('A')
    sobj.Push('B')
    sobj.Push('C')
    sobj.Push('D')

    sobj.Display()
    print("Number of elements in Stack :", sobj.Count())

    print()

    print("Popped Element is :", sobj.Pop())
    sobj.Display()
    print("Number of elements in Stack :", sobj.Count())


if __name__ == "__main__":
    main()