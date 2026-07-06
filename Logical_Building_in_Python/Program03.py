def Summation(No):

    for i in range(1,No+1):
        print(i)
    return

def main():
    Value = 0

    print("Enter number :")
    Value = int(input())

    Ret = Summation(Value)

    print("Summation is : ",Ret)       

if __name__ == "__main__":
    main()        