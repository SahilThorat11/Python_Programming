
def CountCapital(str):

    Count = 0

    for ch in str:
        if(ch >= 65  and ch <= 90):            # ISSUE
            Count = Count + 1

    return Count

def main():
    print("Enter string : ")
    Arr = input()

    Ret = CountCapital(Arr)

    print("Number of capital characters are : ", Ret)

main()