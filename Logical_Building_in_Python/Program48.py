# Input : 4 4

#    a a a a
#    B B B B
#    c c c c
#    D D D D


def Display(iRow,iCol):
    
    ch1 = 'a'
    ch2 = 'A'

    for i in range(iRow):
        for j in range(iCol):
            if((i % 2) == 0):
                print(ch1,"\t",end="") 
            else:
                print(ch2,"\t",end="")   
        print("\n")
        ch1 = chr(ord(ch1) + 1) 
        ch2 = chr(ord(ch2) + 1)    
   

def main():

    print("Enter number of rows:")
    Value1 = int(input())

    print("Enter number of cloumns:")
    Value2 = int(input())

    Display(Value1,Value2)

if __name__ == "__main__":
    main()        