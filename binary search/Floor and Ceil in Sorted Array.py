'''Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
'''

arr= [3,4]
target = 5

def insertPos(arr, target):
    low = 0
    high = len(arr)-1
    floor = -1
    ceil = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return arr[mid], arr[mid]
        elif arr[mid] > target:
            ceil = arr[mid]
            high = mid-1
        else:
            floor = arr[mid]
            low = mid+1  
            
    return floor, ceil
    
print(insertPos(arr, target))

'''
ceil  = the smallest value which is larger than the target (i.e.. target >= arr[mid])
floor = the largest value which is smaller than the target (i.e.. target <= arr[mid])

If element is already present in the array, the floor & ceil are same as the target.

We store the value of each index in 2 variables, as we need to keep track until we met with the condition:
                target <= arr[mid]; 
                target >= arr[mid];
as it will help us return the last known best value

If floor or ceil isn't found, -1 will be returned, if the array doesnt contain the required values necessary to meet the condition.
'''
