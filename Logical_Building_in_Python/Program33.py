# Input : 4
# Output : -4 -3 -2 -1 0 1 2 3 4 

def Display(No):

    if (No < 0):
        No = - No

    i = No
    for i in range(-No,0):
        print(i,"\t",end="")
    
    for i in range(No+1):
        print(i,"\t",end="")
    print("\n")    
   
def main():
    Value = 0

    print("Enter Frequency : ")
    Value = int(input())

    Display(Value)
    
if __name__ == "__main__":
    main()        