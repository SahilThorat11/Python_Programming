def ReverseDigits(No):
    iDigit = 0
    iRev = 0

    if(No < 0):
        No = - No

    while(No != 0):
        iDigit = No % 10
        iRev = iRev * 10 + iDigit
        No = No // 10
    
    return iRev

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = ReverseDigits(Value)

    print("Number of digits are : ",Ret)
    
if __name__ == "__main__":
    main()        