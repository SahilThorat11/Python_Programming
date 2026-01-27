
def CountCapital(str):

    Count = 0

    for ch in str:
        if(ord(ch) >= 65  and ord(ch) <= 90):            # ord() gives ascii value
            Count = Count + 1

    return Count

def main():
    print("Enter string : ")
    Arr = input()

    Ret = CountCapital(Arr)

    print("Number of capital characters are : ", Ret)

main()