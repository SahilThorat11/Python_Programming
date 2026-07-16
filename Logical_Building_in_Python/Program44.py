# Input : 4 4

#    1 * 3  *
#    1 * 3  *
#    1 * 3  *
#    1 * 3  *


def Display(iRow,iCol):
    
    for i in range(iRow):
        for j in range(iCol):
            if((j % 2) == 0):
                print("*\t",end="")
            else:
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