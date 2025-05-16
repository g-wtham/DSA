# %%

n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
    
# %%
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
n = 5
for i in range(n):
    for j in range(1, i+2):
        print(j, end=" ")
    print()

'''
0 1, 2 -> 1
1 1, 3 -> 1,2
2 1, 4 -> 1,2,3
3 1, 5 -> 1,2,3,4
4 1, 6 -> 1,2,3,4,5
'''

# %%
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
    
# %%
n = 5
for i in range(n):
    print("*" * (n-i), end=" ")
    print()
    
n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
    
# %%
    
n = 5
for i in range(n):
    for j in range(1, n-i+1):
        print(j, end=" ")
    print()
     
# %%
   
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
    
# %%

n = 5
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for _ in range(2*n-(2*i+1)):
        print("*", end="")
    for j in range(i):
        print("",end=" ")
    print()
    
'''
9 - 1
7 - 3
5 - 5
3 - 7
1 - 9
'''
    
#%%
n = 5
for i in range(2*n):
    stars = i
    if i > 5:
        stars = 2*n-i
    for j in range(stars):
        print("*",end=" ")
    print()
    
#%%

for i in range(5):
    start = 1
    if i%2 == 0:
        start = 0
    for j in range(i+1):
        print(start, end=" ")
        start = 1 - start
    print()
    
# %%
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for _ in range(2*n-(2*i)):
        print(" ",end="")
    print()
# %%
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for _ in range(2*n-(2*i)):
        print(" ",end="")
    for k in range(1, i+1):
        print(k, end=" ")
    print()

# %%
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for _ in range(2*n-(2*i)):
        print(" ",end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()
    
# %%
for i in range(1, 4+1):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# %%
n = 5
start = 'A'
for i in range(n):
    for j in range(ord(start)+i):
        print(j)
        j += 1
    print()
# %%
n = 5
start = 'A'
for i in range(1, n+1):
    for j in range(ord(start), ord(start)+i):
        print(chr(j), end=" ")
        j += 1
    print()
    
# %%
n = 5
for i in range(n):
    start_char = ord('A') + i
    for j in range(i+1):
        current_start = start_char + j
        print(chr(current_start) , end=" ")
    print()
#%%
n = 5
char = 'A'
number = 0
for i in range(n):
    for j in range(i+1):
        print(chr(ord(char)+number), end=" ")
        number += 1
    print()
    
'''
a 
b c

0
1 2

ch="A"

ch+0         1   A
ch+1 ch+2    2   B C
'''

# %%

n = 5
char = 'A'
for i in range(n):
    for j in range(i+1):
        print(chr(ord(char)+i), end=" ")
    print()



'''
a
bb
ccc

0
1 1
2 2 2

ch="A"

ch+0           1
ch+1 ch+2      2
'''

#%%

n = 5
char = 'A'
for i in range(n):
    print(" " * (n-i), end=" ")
    for k in range(i):
        print(chr(ord(char)+k), end="")
    for k in range(i, -1, -1):
        print(chr(ord(char)+k), end="")
    print()
    
    
'''
1. First inner loop dont print at i=0 and starts printing from 2nd row.
2. Second inner loop prints from i=0, starting from 1st row

[first loop nothing][A]
                 [A][B A]
               [A B][C B A]

[space][ele][space]

    3 1 3
    2 3 2
    1 5 1
    0 7 0

 [   ]1[   ]
    1 2 1
  1 2 3 2 1
'''
# %%
n = 5
char = 'E'
for i in range(n):
    for k in range(i, -1, -1):
        print(chr(ord(char)-k), end="")
    print()
    
# %%

for i in range(n):
    for j in range(n-i, 0, -1):
        print("*", end=" ")
    for j in range(n, 0, -1):
        print("*", end=" ")
    print()
# %%
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * i)
# %%
n = 5

for i in range(n):
    for j in range(n-i, 0, -1):
        print("*", end="")
    for _ in range(2*i):
        print(" ", end="")
    for k in range(n-i, 0, -1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    for _ in range(2*(n-i-1)):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()

    
# %%

# ButterFly Pattern

n = 5

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    for j in range(2*(n-i-1)):
        print(" ",end="")
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i):
        print("*", end="") 
    print()

# %%
n = 5
start = 5
for i in range(n, 0, -1):
    print(" "*(i-1), end="")
    for j in range(i, n+1):
        print(j, end="")
    print()
# %%
