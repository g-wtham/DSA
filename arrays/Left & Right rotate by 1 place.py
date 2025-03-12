# Left rotate by 1 place

arr = [2,3,4,5]
print("Initial Array: ", arr)

first = arr[0]
for i in range(1, len(arr)):
    arr[i-1] = arr[i]
arr[-1] = first
    
print("Left", arr)

# Right rotate by 1 place

arr1 = [2,3,4,5]

last = arr1[-1]
for i in range(len(arr1)-1, 0, -1):
    arr1[i] = arr1[i-1]
arr1[0] = last
    
print("Right", arr1)

'''
=> arr1[2] = 4 is going to move right, i+1 from i, 
but what is going to be in current position, i -> i = 2, i.e., the previous element [i-1]
so i-1 -> [2-1] = 1 -> arr[1] = 3
so current pos, => arr[i] = arr[i-1]
while next arr[i+1] contains arr[i], it will lead to element being overwritten,
thus the array will be filled-with same `i` elements till the end for right rotation,

whereas in left rotation, as we start from index pos -> 1, we assign current element, i to previous pos, i-1
so as `i` in for loop increases, except last element, rest will be having corresponding previous values.
=> arr[i-1] = arr[i]
 
'''