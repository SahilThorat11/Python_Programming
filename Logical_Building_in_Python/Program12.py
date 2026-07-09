def SumFactors(No):

    iSum = 0

    if(No < 0):
        No = -No
        
    for i in range(1,int((No/2)+1)):
        if((No % i == 0)):
            iSum += i

    return iSum        

def main():
    Value = 0

    print("Enter number :")
    Value = int(input())

    Ret = SumFactors(Value)       

    print("Summation of factors : ",Ret)

if __name__ == "__main__":
    main()        