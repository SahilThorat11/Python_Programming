def CheckDivisible(No):

    if((No % 5) == 0):
        return True
    else:
        return False
    
def main():
    Value = 0

    print("Enter number to check whether it is divivble by 5 :")
    Value = int(input())

    Ret = CheckDivisible(Value)
    if(Ret == True):
        print(f"{Value} is divisible by 5")

    else:
        print(f"{Value} is not divisible by 5")        

if __name__ == "__main__":
    main()        