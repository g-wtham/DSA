k = 8
array = [2, 6, 3, 5]
n = len(array)

# To consider single-element subarrays get skipped if i+1, means, if arr = [8], then 0 count is returned, not as 1.
# So, start from range `i`
# In slicing, end is exclusive, so arr[0:1] will return only [2], but we need 2 elements to be added as a valid subarray, to get the target sum, so [i : j+1] 

def Bruteforce_SubarraySum(nums, k):
    count = 0
    for i in range(n):
        for j in range(i, n):
            subarraySum = sum(nums[i:j+1])
            
            if subarraySum == k:
                count += 1

    return count

print(Bruteforce_SubarraySum(array, k))

def subarraySum(nums, k):
        left = 0
        right = 0
        n = len(nums)
        Sum = 0
        count = 0
        while right < n:
            while left <= right and Sum > k:
                Sum -= nums[left]
                left += 1

            if Sum == k:
                count += 1
                
            right += 1
            
            if right < n:
                Sum += nums[right] 
                
            # add the next element to the Sum array.. after Sum == target, as we need to check next successive elements
            # if we move right += 1 inside if block, it will access n-th element and list index out of range will occur.
            # you should check right < n, before trying to access nums[right], moving right += 1 inside if block will cause the out of range error, as there is no way to prevent from accessing the out of bounds value.

        return count

print(subarraySum(array, k))