# Input : 4
# Output : * * * *

def Display(No):

    for i in range(1,No+1):
        print("*\t",end="")
    print("\n")    
   
def main():
    Value = 0

    print("Enter Frequency : ")
    Value = int(input())

    Display(Value)
    
if __name__ == "__main__":
    main()        