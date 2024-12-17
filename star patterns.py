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

def binary_right_triangle():
    n=5
    start = 1
    for i in range(n): #controls the rows
        if i%2 == 0:
            start = 1
        else:
            start = 0
        
        for j in range(i+1): 
            
            '''
            If i+1 is not given and if its range(i), then for range(i) -> [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]. [0, 1, 2, 3, 4] ~ n=5 
            (Loop ran 5 times). But, in range([0]), no element is printed as it is an empty range.
            And, start variable is altered and logic gets reversed. Only 4 visible lines of alternate 1s and 0s are printed.
            '''
            print(start, end=" ")
            start = 1 - start
        print()
        
binary_right_triangle()

def crown_pattern():
    '''
    Outer loop : n -> 4

    [1, 0, 0, 0, 0, 0, 0, 1]
    [1, 2, 0, 0, 0, 0, 2, 1]
    [1, 2, 3, 0, 0, 3, 2, 1]
    [1, 2, 3, 4, 4, 3, 2, 1]

    Inner loops:
        i. 1st loop - Numbers -> [1, (i+1)]
        ii. 2nd loop - Space [6, 4, 2, 0] -> [2 * n - (2 * i + 2)]
        iii. 3rd loop - Numbers -> [i+1, 0, -1]

    (Outer loop)
        (Inner loop)
        (New line)
    --- start next iteration ---
   
    '''
    n = 4
    for i in range(n):
        for x in range(1, i+2):
            print(x, end="")
        for y in range(2 * n - (2 * i + 2)):
            print(" ", end="")
        for z in range(i+1, 0, -1):
            print(z, end="")
        print()
        
# Key moment: Solved the entire problem without looking up any reference. 
# Came up with formulas and structure, everything on own.

crown_pattern()