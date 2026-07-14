# Input : 4 #
#  Output : # # # # 

#  Input : 5 &
#  Output : & & & & & 

#  Input : 3 z
#  Output : z z z

def Display(No,ch):

    if (No < 0):
        No = - No

    i = No
    for i in range(1,No+1):
        print(ch,"\t",end="")
    print("\n")    
   
def main():
    Value = 0

    print("Enter Frequency : ")
    Value = int(input())

    print("Enter Character : ")
    cValue = input()

    print("Accepted character is : ",cValue)

    Display(Value,cValue)
    
if __name__ == "__main__":
    main()        