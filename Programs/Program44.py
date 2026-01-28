
def ConvertLowerCase(Brr):
    Result = ""

    for ch in Brr:
        if(ch >= 'A' and ch <= 'Z'):
            Result = Result + chr(ord(ch) + 32)
        else:
            Result = Result + ch

    return Result

def main():
    print("Enter string : ")
    Arr = input()

    Ret = ConvertLowerCase(Arr)

    print("Updated string is : ", Ret)

main()