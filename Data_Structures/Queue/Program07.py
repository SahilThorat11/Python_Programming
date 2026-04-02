class QueueNode:
    def __init__(self, no):
        self.data = no
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.iCount = 0

    def enqueue(self, no):
        newn = QueueNode(no)

        if self.first is None:  # instead of '=='
            self.first = newn
        else:
            temp = self.first
            while temp.next is not None:    # instead of '!='
                temp = temp.next
            temp.next = newn

        self.iCount += 1    # instead of 'self.iCount = self.iCount + 1'

    def dequeue(self):
        if self.first is None:  # instead of '=='
            print("Queue is empty")
            return -1

        value = self.first.data
        temp = self.first

        self.first = self.first.next
        del temp

        self.iCount -= 1        # instead of 'self.iCount = self.iCount - 1'
        return value

    def display(self):
        if self.first is None:      # instead of '=='
            print("Queue is empty")
            return

        temp = self.first
        print()

        while temp is not None:     # instead of '!='
            print(f"| {temp.data} | -", end="")
            temp = temp.next

        print()

    def count(self):
        return self.iCount


def main():
    qobj = Queue()

    qobj.enqueue(11)
    qobj.enqueue(21)
    qobj.enqueue(51)
    qobj.enqueue(101)

    qobj.display()
    print("Number of elements in Queue :", qobj.count())

    print()
    
    print("Removed Element is :", qobj.dequeue())
    qobj.display()
    print("Number of elements in Queue :", qobj.count())

    print()

    print("Removed Element is :", qobj.dequeue())
    qobj.display()
    print("Number of elements in Queue :", qobj.count())

    qobj.enqueue(121)

    qobj.display()
    print("Number of elements in Queue :", qobj.count())


if __name__ == "__main__":
    main()