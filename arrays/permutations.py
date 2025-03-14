def permute(nums, path=[]):
    if not nums:
        print(path)  # Base case: print the permutation
        return

    for i in range(len(nums)):
        permute(nums[:i]+nums[i+1:], path + [nums[i]])

permute([1,2,3])