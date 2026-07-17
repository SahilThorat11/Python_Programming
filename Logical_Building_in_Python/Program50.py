# Input : 4 4

#     * * * *
#     0 0 0 0
#     0 0 0 0
#     0 0 0 0
#     * * * *

class Pattern:

    def Display(self,iRow,iCol):

        for i in range(iRow):
            for j in range(iCol):
                if((i == 0) or (i == iRow-1)):
                    print("*\t",end="")
                else:
                    print("o\t",end="")
            print("\n")   
   

def main():

    print("Enter number of rows:")
    Value1 = int(input())

    print("Enter number of cloumns:")
    Value2 = int(input())

    pobj = Pattern()

    pobj.Display(Value1,Value2)

if __name__ == "__main__":
    main()        