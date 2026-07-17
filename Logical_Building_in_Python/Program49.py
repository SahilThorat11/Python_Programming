# Input : 4 4

#    1 2 3 4
#    5 6 7 8
#    9 10 11 12
#    13 14 15 16


def Display(iRow,iCol):

    iCnt = 1

    for i in range(iRow):
        for j in range(iCol):
            print(iCnt,"\t",end="")
            iCnt += 1

        print("\n")   
   

def main():

    print("Enter number of rows:")
    Value1 = int(input())

    print("Enter number of cloumns:")
    Value2 = int(input())

    Display(Value1,Value2)

if __name__ == "__main__":
    main()        