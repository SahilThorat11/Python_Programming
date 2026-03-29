
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
        pass

    def peep(self):
        pass

    def Display(self):
        temp = self.first

        if(self.first is None):
            print("Stack is empty")
            return

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


if __name__ == "__main__":
    main()