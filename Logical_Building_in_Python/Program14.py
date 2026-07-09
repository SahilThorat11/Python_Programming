def CheckPrime(No):

    bFlag = True

    if(No < 0):
        No = -No
        
    for i in range(2,int((No/2)+1)):   # ISSUE
        if((No % i == 0)):
            bFlag = False
            break
    
    return bFlag       

def main():
    Value = 0

    print("Enter number :")
    Value = int(input())

    Ret = CheckPrime(Value)       
    if(Ret == True):
        print(f"{Value} is prime number")
    else:
        print(f"{Value} is not a prime number")

if __name__ == "__main__":
    main()        