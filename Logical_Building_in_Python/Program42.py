def Display(iRow,iCol):
    
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            print(j,"\t",end="")
        print("\n")

            
def main():

    print("Enter number of rows:")
    Value1 = int(input())

    print("Enter number of cloumns:")
    Value2 = int(input())

    Display(Value1,Value2)

if __name__ == "__main__":
    main()        