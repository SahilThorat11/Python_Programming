def CheckPerfect(No):

    iSum = 0

    if(No < 0):
        No = -No
        
    for i in range(1,int((No/2)+1)):
        if((No % i == 0)):
            iSum += i

    return (iSum == No)       

def main():
    Value = 0

    print("Enter number :")
    Value = int(input())

    Ret = CheckPerfect(Value)       
    if(Ret == True):
        print(f"{Value} is perfect number")
    else:
        print(f"{Value} is not a perfect number")

if __name__ == "__main__":
    main()        