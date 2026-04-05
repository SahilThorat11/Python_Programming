class InsertionSort:
    def sort(self, arr):
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while(j >= 0 and arr[j] > key):
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key


def main():
    iValue = int(input("Enter number of elements: "))

    arr = []
    print(f"Enter {iValue} elements:")

    for _ in range(iValue):
        arr.append(int(input()))

    iobj = InsertionSort()
    iobj.sort(arr)

    print("Sorted array:", end=" ")
    for num in arr:
        print(num, end=" ")


if __name__ == "__main__":
    main()