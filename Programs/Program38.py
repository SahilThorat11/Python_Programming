
def CountCapital(str):

    Count = 0

    for i in range(len(str)):
        if(str[i] >= 'A'  and str[i] <= 'Z'):
            Count = Count + 1

    return Count

def main():
    print("Enter string : ")
    Arr = input()

    Ret = CountCapital(Arr)

    print("Number of capital characters are : ", Ret)

main()