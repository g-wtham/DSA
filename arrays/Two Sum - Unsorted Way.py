nums = [3, 2, 4]
target = 5
dict1 = {}

for i in range(len(nums)):
    if nums[i] not in dict1:
        dict1[nums[i]] = i
        
    required = target - nums[i]
    if required in dict1:
        print(dict1[required], i)
        
        for k, v in dict1.items():
            if k == required:
                key_value = k
                
        print(key_value, nums[i])