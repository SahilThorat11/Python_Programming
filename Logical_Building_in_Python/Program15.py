def CheckPrime(No):

    if(No < 0):
        No = -No

    i = 0        
    for i in range(2,int((No/2)+1)):
        if((No % i == 0)):
            return False
    
    return True      

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