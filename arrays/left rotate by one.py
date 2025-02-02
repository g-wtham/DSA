arr = [1,2,3,4,5]

'''
1. First element goes to the last index (left rotation by 1), and remaining elements moves one index backward (i-1)
2. Thus, always store the 1st element in a 'temp' variable so after len(arr) iterations, for the last index, we can put the first element there.

2, 3, 4, 5, _
2, 3, 4, 5, [temp_variable = 1]
'''

def leftRotatebyOne(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    
    return arr

print(leftRotatebyOne(arr))

arr1 = [1,2,3,4,5]

def leftRotatebyK(arr, k):
    n = len(arr)
    k = k % n # To reduce the rotation steps, if k > n i.e. 21 > 5 == effects similar to 1 rotation ..
    temp = arr[0:k]
    
    for i in range(k, n):
        arr[i-k] = arr[i]
        
    j = 0    
    for z in range(n-k, n):
        arr[z] = temp[j]
        j += 1
        
    return arr

print(leftRotatebyK(arr1, 2))

