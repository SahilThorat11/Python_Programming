def CountSumDigits(No):
    iDigit = 0
    iSum = 0

    while(No != 0):
        iDigit = No % 10
        iSum += iDigit
        No = No // 10
    
    return iSum

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = CountSumDigits(Value)

    print("Number of digits are : ",Ret)
    
if __name__ == "__main__":
    main()        