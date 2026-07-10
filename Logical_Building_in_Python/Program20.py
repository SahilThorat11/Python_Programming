def CountEvenDigits(No):
    iDigit = 0
    iCnt = 0

    while(No != 0):
        iDigit = No % 10
        if((iDigit % 2) == 0):
            iCnt += 1
        No = No // 10
    
    return iCnt

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = CountEvenDigits(Value)

    print("Number of even digits are : ",Ret)
    
if __name__ == "__main__":
    main()        