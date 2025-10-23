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
# Increasing and Decreasing Order

arr = [8, 7, 1, 6, 5, 9]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

arr[len(arr)//2:] = reversed(arr[len(arr)//2:])

print(arr)

# %%

# Find the median of an array

arr = [8, 7, 1, 6, 5, 9]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]

if len(arr) % 2 == 0:
    print(float( (arr[len(arr)//2] + arr[(len(arr)//2) - 1]) / 2 ) )
else:
    print(arr[len(arr)//2])


# %%
# EXTRA TIME METHOD - remove duplicates from sorted array and unsorted array
 
result = []
arr = [2,3,1,9,3,1,3,9]

for ele in arr: 
    if ele not in result:
        result.append(ele)

print(result)

# %%

# EXTRA SPACE METHOD - remove duplicates from sorted array and unsorted array

seen = set()
unique = []
for ele in arr:
    if ele not in seen:
        seen.add(ele)
        unique.append(ele)
print(unique)

# %%

arr = [1,2,3,4,5]
n = 6

def insert_at_start(arr, value):
    copy_arr = arr
    arr = [0] * (len(arr) + 1)

    arr[0] = value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    for i in range(len(copy_arr)):
        arr[i+1] = copy_arr[i]

    return arr

print(insert_at_start(arr, n))

def insert_at_end(arr, value):
    copy_arr = arr
    arr = [0] * (len(arr) + 1)
    arr[len(arr)-1] = value   

    for i in range(len(copy_arr)):
        arr[i] = copy_arr[i]

    return arr

print(insert_at_end(arr, n))

# [1, 2, 4, 5] -> 3rd pos - 3 -> 0,1,2 => position_index = pos - 1 
def insert_at_specific(arr, val, pos):
    n = len(arr)
    new_arr = [0] * (n+1) 

    for i in range(pos):
        new_arr[i] = arr[i]

    new_arr[pos] = val
    
    for i in range(pos, len(arr)):
        new_arr[i+1] = arr[i]

    return new_arr
    
print(insert_at_specific(arr, n, 3))

# %%
