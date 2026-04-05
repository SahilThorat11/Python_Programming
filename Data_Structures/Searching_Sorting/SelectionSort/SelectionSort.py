class SelectionSort:
    def sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            index_of_min = i

            for j in range(i + 1, n):
                if arr[j] < arr[index_of_min]:
                    index_of_min = j

            # swap
            temp = arr[i]
            arr[i] = arr[index_of_min]
            arr[index_of_min] = temp


def main():
    iValue = int(input("Enter number of elements: "))

    arr = []
    print(f"Enter {iValue} elements:")

    for _ in range(iValue):
        arr.append(int(input()))

    ssobj = SelectionSort()
    ssobj.sort(arr)

    print("Sorted array:", end=" ")
    for num in arr:
        print(num, end=" ")


if __name__ == "__main__":
    main()