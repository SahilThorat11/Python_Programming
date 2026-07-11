# Input : 4
# Output : 1 2 3 4

def Display(No):

    if (No < 0):
        No = - No

    for i in range(1,No):
        print(i,"\t",end="")
    print("\n")    
   
def main():
    Value = 0

    print("Enter Frequency : ")
    Value = int(input())

    Display(Value)
    
if __name__ == "__main__":
    main()        