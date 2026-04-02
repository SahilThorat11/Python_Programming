class QueueNode:
    def __init__(self, no):
        self.data = no
        self.next = None


class Queue:
    def __init__(self):
        print("Queue gets created successfully...\n")
        self.first = None
        self.iCount = 0

    def enqueue(self, no):
        newn = QueueNode(no)

        if(self.first == None):
            self.first = newn
        else:
            temp = self.first
            while(temp.next != None):
                temp = temp.next
            temp.next = newn

        self.iCount = self.iCount + 1

    def dequeue(self):
        pass

    def display(self):
        pass

    def count(self):
        pass


def main():
    qobj = Queue()
    
    qobj.enqueue(11)
    qobj.enqueue(21)
    qobj.enqueue(51)
    qobj.enqueue(101)

if __name__ == "__main__":
    main()