arr = [12, 35, 1, 10, 34, 1]

def second_lar(arr):
    max = float('-inf')
    second_largest = float('-inf')
    
    for item in arr:
        if item > max:
            second_largest = max
            max = item
        elif max > item > second_largest:
            second_largest = item
            
    return second_largest

print(second_lar(arr))
    
arr1 = [0, 1, 0, 3, 12]

def move_zeroes(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[k] = arr[i]
            k+=1
    for j in range(k, len(arr)):
        arr[j] = 0
        
    return arr

print(move_zeroes(arr1))
    
arr2 = [-2,1,-3,4,-1,2,1,-5,4]

def kadane_max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    start = 0
    temp_start = 0
    end = 0
    
    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i]
            temp_start = i
            
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
            
    return max_sum, arr[start: end+1]

print(kadane_max_subarray_sum(arr2))

arr3 = [1, 2, 3, 4, 5]
D = 2
output = [3,4,5,1,2]

def left_rotate(arr, D):   
    # first = arr[0]
    # second = arr[1]
    # for i in range(len(arr)-D):
    #     arr[i] = arr[i+D]
    # arr[len(arr)-2] =  first
    # arr[len(arr)-1] =  second
    
    # return arr
    n = len(arr)
    D = D % n
    rotated = [0] * n
    
    for i in range(n):
        rotated[i] = arr[(i+D)%n]
        
    return rotated

print(left_rotate(arr3, D))

arr4 = [3,6, 0, 1]
def missing_number(arr):
    for i in range(max(arr)):
        if i not in arr:
            print(i)
    return "end"
            
print(missing_number(arr4))

