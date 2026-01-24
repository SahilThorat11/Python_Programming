
def SumDigit(No):

    iDigit = 0
    iSum = 0

    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10    

    return iSum;         

def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())
    
    iRet = SumDigit(Value)

    print("Summation of digit is : ", iRet)

main() 