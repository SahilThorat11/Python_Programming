# Input : 4 4

#    0 * * *
#    * 0   *
#    *   0 * 
#    * * * 0

class Pattern:

    def Display(self,iRow,iCol):

        if iRow != iCol:
            print("Invaild Input")
            return

        for i in range(iRow):
            for j in range(iCol):
                if i == j:
                    print("o\t",end="")
                else:
                    print("*\t",end="")    
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