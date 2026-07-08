def DisplayFactorsNonFactors(No):

    if(No < 0):
        No = -No
        
    for i in range(1,No+1):
        if((No % i) == 0):
            print("Factors is : ",i)
        else:
            print("Non Factors is :",i)    

def main():
    Value = 0

    print("Enter number :")
    Value = int(input())

    DisplayFactorsNonFactors(Value)       

if __name__ == "__main__":
    main()        