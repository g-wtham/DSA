nums = [2, 7, 11, 15]
target = 26
list1 = []
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == target:
            list1.append(i)
            list1.append(j)
    
print(list1)  

# Optimal approach using HashMap (dict.)

def two_sum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in nums_map:
            return [nums_map[complement], i]     
        
        nums_map[num] = i 
    
print(two_sum(nums, target))