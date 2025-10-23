# %%

# Smallest ele in array 

arr = [2,5,1,3]

min = arr[0]
for ele in arr:
    if ele < min:
        min = ele

print(min)

# %%

# Largest ele in array

arr = [8, 10, 5, 7, 9]
max = arr[0]
for ele in arr:
    if ele > max:
        max = ele

print(max)

# %%

# Find Second Smallest and Second Largest Element in an array

arr = [8, 10, 5, 7, 9]

def secSmall(arr):
    small = float('inf')
    secSmall = float('inf')

    for ele in arr:
        if ele < small:
            secSmall = small
            small = ele

        elif ele < secSmall and ele > small:
            secSmall = ele

    return secSmall

def secLarg(arr):
    largest = float('-inf')
    secLarg = float('-inf')

    for ele in arr:
        if ele > largest:
            secLarg = largest
            largest = ele

        elif ele > secLarg and ele < largest:
            secLarg = ele

    return secLarg

print(secLarg(arr))
print(secSmall(arr))

# %%

# Reverse an array - O(n) Time & O(1) Space

arr = [10,20,30,40]

p1 = 0
p2 = len(arr) - 1
while p1 < p2:
    arr[p1], arr[p2] = arr[p2], arr[p1]
    p1 += 1
    p2 -= 1
 
print(arr)

# %%

arr = [8, 7, 1, 6, 5, 9]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

    arr[len(arr)//2:] = reversed(arr[len(arr)//2:])

print(arr)
# %%
