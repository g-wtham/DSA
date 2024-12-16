'''

Inverted Star Triangle :

ol :
    rows - 5
    i loop (n)
in :
    1st : space
    2nd : 2 * N - (2 * i + 1)
    3rd : space
    
'''

n = 5
for i in range(n):
    for x in range(i):
        print(" ", end="")
    for y in range(2 * n - (2 * i +1)):
        print("*", end="")
    for z in range(i):
        print(" ", end="")
    print()