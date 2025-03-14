# Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

# Bruteforce - Linear Search 
arr1 = [4,1,2,1,2]

for i in range(len(arr1)):
    count = 0
    for j in range(len(arr1)):
        if arr1[i] == arr1[j]:
            count += 1
            
    if count == 1:
        print(arr1[i]) 
    

# Optimal Approach
arr = [4,1,2,1,2]

xor = 0
for item in arr:
    xor ^= item
print(xor)

'''
xor => 2 properties : 1. same numbers -> 1 ^ 1 = 0 (or) 0 ^ 0 = 0
                      2. different numbers -> a ^ 0 = a (or) a ^ 1 = a

0 -> 0000
4 -> 0100
1 -> 0001
2 -> 0010
'''

arr1 = [4,1,2,1,2]
seen = set()
duplicates = set()
for item in arr1:
    if item not in seen:
        seen.add(item)
    else:
        duplicates.add(item)
        
for item in seen:
    if item not in duplicates:
        print(item)