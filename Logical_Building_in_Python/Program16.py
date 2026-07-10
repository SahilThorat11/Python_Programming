def main():
    No = 751
    iDigit = 0

    iDigit = No % 10
    print("Digit is : ",iDigit)
    No = No // 10
    print("Updated No : ",No)

    iDigit = No % 10
    print("Digit is : ",iDigit)
    No = No // 10
    print("Updated No : ",No)
        
    iDigit = No % 10
    print("Digit is : ",iDigit)
    No = No // 10
    print("Updated No : ",No)
    
if __name__ == "__main__":
    main()        