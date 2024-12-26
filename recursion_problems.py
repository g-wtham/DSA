def printNos(n):
    if n==1:
        print("1 to N using recursion: ")
        print("1", end=" ")
    else:
        printNos(n-1)
        print(n, end=" ")
        
printNos(20)
      
print("\n")
print("N to 1 using recursion: ")
def printNos(n):
    if n==1:
        print("1", end=" ")
    else:
        print(n, end=" ")
        printNos(n-1)
printNos(20)

# Once the base case reaches, the function unwinds, which then goes to the next line to execute, till that it keeps running recursively