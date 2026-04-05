class BubbleSort:
    def sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if(arr[j] > arr[j + 1]):
                    # swap
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp


def main():
    
    iValue = int(input("Enter number of elements: "))

    arr = []
    print(f"Enter {iValue} elements:")
    
    for _ in range(iValue):
        arr.append(int(input()))

    bobj = BubbleSort()
    bobj.sort(arr)

    print("Sorted array:", end=" ")
    for num in arr:
        print(num, end=" ")


if __name__ == "__main__":
    main()