# Input : 4 4

#   o o o *
#   o o * *
#   o * * *        
#   * * * *

class Pattern:

    def Display(self,iRow,iCol):

        if iRow != iCol:
            print("Invaild Input")
            return

        for i in range(1,iRow + 1):
            for j in range(iCol,0,-1):
                if i >= j:
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