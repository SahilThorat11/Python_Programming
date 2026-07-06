def Summation(No):

    sum = 0

    for i in range(1,No+1):
        sum += i
    
    return sum

def main():
    Value = 0

    print("Enter number :")
    Value = int(input())

    Ret = Summation(Value)

    print("Summation is : ",Ret)       

if __name__ == "__main__":
    main()        