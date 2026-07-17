# Input : 4 4

#    a a a a
#    b b b b
#    c c c c
#    d d d d


def Display(iRow,iCol):
    
    ch = 'a'
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