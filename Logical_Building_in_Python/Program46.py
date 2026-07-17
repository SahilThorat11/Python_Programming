# Input : 4 4

#    A A A A
#    B B B B
#    C C C C
#    D D D D


def Display(iRow,iCol):
    
    ch = 'A'
    for i in range(iRow):
        for j in range(iCol):
            print(ch,"\t",end="") 
        print("\n")
        ch = chr(ord(ch) + 1)    

            
def main():

    print("Enter number of rows:")
    Value1 = int(input())

    print("Enter number of cloumns:")
    Value2 = int(input())

    Display(Value1,Value2)

if __name__ == "__main__":
    main()        