# Input : 4 4

#    A B C D
#    A B C D
#    A B C D
#    A B C D


def Display(iRow,iCol):
    
    for i in range(iRow):
        ch = 'A'
        for j in range(iCol):
            print(ch,"\t",end="") 
            ch = chr(ord(ch) + 1)
        print("\n")

            
def main():

    print("Enter number of rows:")
    Value1 = int(input())

    print("Enter number of cloumns:")
    Value2 = int(input())

    Display(Value1,Value2)

if __name__ == "__main__":
    main()        