
def CountCapital(str):

    Count = 0

    for i in range(len(str)):
        if(str[i] >= 65  and str[i] <= 90):            # ISSUE
            Count = Count + 1

    return Count

def main():
    print("Enter string : ")
    Arr = input()

    Ret = CountCapital(Arr)

    print("Number of capital characters are : ", Ret)

main()