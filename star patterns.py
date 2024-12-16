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

def inverted_triangle():
    n = 5
    for i in range(n):
        for x in range(i):
            print(" ", end="")
        for y in range(2 * n - (2 * i +1)):
            print("*", end="")
        for z in range(i):
            print(" ", end="")
        print()

inverted_triangle()
    
'''
Diamond shaped triangle :

ol : range(n) -> rows -> n
il : 
    1st loop: space
    2nd loop: stars
    3rd loop: space
    
repeat for inverted triangle

[4, 1, 4] 0 -> as 1 = +1
[3, 3, 3] 1 -> as 3 = +2
[2, 5, 2] 2 -> as 5 + +3
[1, 7, 1] 3
[0, 9, 0] 4 
'''
def diamond_triangle():
    n = 5
    for i in range(n):
        for x in range(n-1-i):
            print(" ", end="")
        for y in range(2 * i + 1):
            print("*", end="")
        for z in range(n-1-i):
            print(" ", end="")
        print()
    inverted_triangle()

diamond_triangle()
        
def half_diamond_pattern():
    n = 5
    for i in range(2*n):
        stars = i
        if i > n:
            stars = 2 * n - i
        for j in range(stars):
            print("*", end=" ")
        print()
        
half_diamond_pattern()