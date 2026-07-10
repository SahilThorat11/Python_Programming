def CountDigits(No):
    iDigit = 0
    iCnt = 0
    
    while(No != 0):
        iDigit = No % 10
        No = No // 10
        iCnt += 1

    return iCnt

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = CountDigits(Value)

    print("Number of digits are : ",Ret)
    
if __name__ == "__main__":
    main()        