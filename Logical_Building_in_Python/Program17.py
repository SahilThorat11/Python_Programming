def DisplayDigits(No):
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        print(iDigit)
        No = No // 10

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    DisplayDigits(Value)
    
if __name__ == "__main__":
    main()        