ERR_INVALID = -1

def Factorial(No):

    Fact = 1

    if (No < 0):
        return ERR_INVALID

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Value = 0

    print("Enter number :")
    Value = int(input())

    Ret = Factorial(Value)
    if(Ret == ERR_INVALID):
        print("Invaild input")
    else:
        print("Factorial is : ",Ret)       

if __name__ == "__main__":
    main()        