
def CountSmall(str):

    Count = 0

    for i in range(len(str)):
        if(str[i] >= 'a' and str[i] <= 'z'):
            Count = Count + 1

    return Count

def main():
    print("Enter string : ")
    Arr = input()

    Ret = CountSmall(Arr)

    print("Number of Small characters are : ", Ret)

main()